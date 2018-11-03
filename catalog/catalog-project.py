from flask import (Flask, render_template, request, redirect,
                   url_for, flash, jsonify)
from flask import session as loginSession, make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from database_setup import Base, Competition, Athlete, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
              open('client_secrets.json', 'r').read())['web']['client_id']
Application_Name = "Top Flight Sports Catalog Application"

# Establish a Connection to the Database
engine = create_engine('sqlite:///sportscatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create a State Token for Anti-Forgery
@app.route('/login')
def loginPage():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    loginSession['state'] = state
    # return "The current session state is %s" % loginSession['state']
    return render_template('login.html', STATE=state)


# User Assist Functions
def createUser(loginSession):
    newUser = User(name=loginSession['username'], email=loginSession[
                   'email'], picture=loginSession['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=loginSession['email']).one()
    return user.userID


def getUserInfo(userID):
    user = session.query(User).filter_by(userID=userID).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.userID
    except:
        return None


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate State Token
    if request.args.get('state') != loginSession['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the Authorization Code into a Credentials Object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the Access Token is Valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an Error in the Access Token Info, Abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the Access Token is used for the Intended User.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the Access Token is Valid for this App.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = loginSession.get('access_token')
    stored_gplus_id = loginSession.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                    json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the Access Token in the Session for Later Use.
    loginSession['access_token'] = credentials.access_token
    loginSession['gplus_id'] = gplus_id

    # Get User Info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    loginSession['username'] = data['name']
    loginSession['picture'] = data['picture']
    loginSession['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    loginSession['provider'] = 'google'

    # See if User Exists, if it doesn't Make a New One
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(loginSession)
    loginSession['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += loginSession['username']
    output += '!</h1>'
    output += '<img src="'
    output += loginSession['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;' \
        '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You Are Now Logged In As %s" % loginSession['username'])
    print "Done!"
    return output


# DISCONNECT - Revoke a current user's token and reset their loginSession
@app.route('/gdisconnect')
def gdisconnect():
    # Only Disconnect a Connected User.
    access_token = loginSession.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Create JSON API endpoint for All Sports
@app.route('/sports/JSON')
def allSportsJSON():
    sport = session.query(Competition).all()
    return jsonify(sport=[i.serialize for i in sport])


# Create JSON API for an Individual Sport
@app.route('/sports/<int:sportID>/JSON')
def sportJSON(sportID):
    sport = session.query(Competition).filter_by(sportID=sportID).one()
    return jsonify(Competition=sport.serialize)


# Create JSON API endpoint for All players in a Sport
@app.route('/sports/<int:sportID>/player/JSON')
def sportPlayersJSON(sportID):
    sport = session.query(Competition).filter_by(sportID=sportID).one()
    player = session.query(Athlete).filter_by(sport_id=sportID).all()
    return jsonify(Athlete=[i.serialize for i in player])


# Create JSON API endpoint for an Individual player in a Sport
@app.route('/sports/<int:sportID>/player/<int:playerID>/JSON')
def playerJSON(sportID, playerID):
    player = session.query(Athlete).filter_by(playerID=playerID).one()
    return jsonify(Athlete=player.serialize)


@app.route('/')
@app.route('/sports')
def sportsHome():
    sportMain = session.query(Competition).all()
    return render_template('index.html', items=sportMain)


# List CURRENT Players for a slected Sport
@app.route('/sports/<int:sportID>/player')
def sportPlayer(sportID):
    sport = session.query(Competition).filter_by(sportID=sportID).one()
    player = session.query(Athlete).filter_by(sport_id=sportID).all()
    if 'username' not in loginSession:
        return render_template('publicSports.html',
                               items=player, sport=sport, sportID=sportID)
    else:
        return render_template('sports.html',
                               sport=sport, sportID=sportID, items=player)


# Method for Creating a NEW Player
@app.route('/sports/<int:sportID>/new', methods=['GET', 'POST'])
def newPlayer(sportID):
    if 'username' not in loginSession:
        return redirect('/login')
    sport = session.query(Competition).filter_by(sportID=sportID).one()
    creator = loginSession['user_id']
    if request.method == 'POST':
        newPlayer = Athlete(name=request.form['name'], position=request.form[
                           'position'], team=request.form['team'],
                           career_stats=request.form['career_stats'],
                           sport_id=sportID, user_id=creator)
        session.add(newPlayer)
        session.commit()
        flash("%s Has Been Created!" % (newPlayer.name))
        return redirect(url_for('sportPlayer', sportID=sportID))
    else:
        return render_template('newPlayer.html', sportID=sportID)


# Method for EDITING a Player
@app.route('/sports/<int:sportID>/<int:playerID>/edit',
           methods=['GET', 'POST'])
def editPlayer(sportID, playerID):
    if 'username' not in loginSession:
        return redirect('/login')
    editedPlayer = session.query(Athlete).filter_by(playerID=playerID).one()
    creator = loginSession['user_id']
    if creator != editedPlayer.user_id:
        flash("You are not authorized to this edit player. Please login and "
              "edit your own created players.")
        return redirect(url_for('sportPlayer', sportID=sportID))
    if request.method == 'POST':
        if request.form['name']:
            editedPlayer.name = request.form['name']
        if request.form['position']:
            editedPlayer.position = request.form['position']
        if request.form['team']:
            editedPlayer.team = request.form['team']
        if request.form['career_stats']:
            editedPlayer.career_stats = request.form['career_stats']
        session.add(editedPlayer)
        session.commit()
        flash("%s Has Been Updated!" % (editedPlayer.name))
        return redirect(url_for('sportPlayer', sportID=sportID))
    else:
        return render_template('editPlayer.html',
                               sportID=sportID, playerID=playerID,
                               item=editedPlayer)


# Method for DELETING a Player
@app.route('/sports/<int:sportID>/<int:playerID>/delete',
           methods=['GET', 'POST'])
def deletePlayer(sportID, playerID):
    if 'username' not in loginSession:
        return redirect('/login')
    sport = session.query(Competition).filter_by(sportID=sportID).one()
    creator = loginSession['user_id']
    deletedPlayer = session.query(Athlete).filter_by(playerID=playerID).one()
    if creator != deletedPlayer.user_id:
        flash("You are not authorized to delete this player. Please login "
              "and delete your own created players.")
        return redirect(url_for('sportPlayer', sportID=sportID))
    if request.method == 'POST':
        session.delete(deletedPlayer)
        session.commit()
        flash("%s Has Been Deleted!" % (deletedPlayer.name))
        return redirect(url_for('sportPlayer', sportID=sportID))
    else:
        return render_template('deletePlayer.html',
                               sportID=sportID, playerID=playerID,
                               item=deletedPlayer)


# Disconnect from application based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in loginSession:
        if loginSession['provider'] == 'google':
            gdisconnect()
            del loginSession['gplus_id']
            del loginSession['access_token']
        del loginSession['username']
        del loginSession['email']
        del loginSession['picture']
        del loginSession['user_id']
        del loginSession['provider']
        flash("You Have Successfully Logged Out.")
        return redirect(url_for('sportsHome'))
    else:
        flash("You Were Not Logged In!")
        return redirect(url_for('sportsHome'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
