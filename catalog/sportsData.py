from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Competition, Athlete, User


engine = create_engine('sqlite:///sportscatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


user1 = User(name="Kevin E.", email="bigsave24@yahoo.com")
session.add(user1)
session.commit()


# Sports for Sports Table
sport1 = Competition(sport="Basketball", user_id=1)
session.add(sport1)
session.commit()

sport2 = Competition(sport="Football", user_id=1)
session.add(sport2)
session.commit()

sport3 = Competition(sport="Soccer", user_id=1)
session.add(sport3)
session.commit()

sport4 = Competition(sport="Hockey", user_id=1)
session.add(sport4)
session.commit()

sport5 = Competition(sport="Baseball", user_id=1)
session.add(sport5)
session.commit()


# Players for Basketball
player1 = Athlete(
                  name="LeBron James", position="Small Forward",
                  team="Los Angeles Lakers",
                  career_stats="PPG: 27.2 | APG: 7.2 | RPG: 7.4",
                  sport=sport1, user_id=1)
session.add(player1)
session.commit()

player2 = Athlete(
                  name="Stephen Curry", position="Point Guard",
                  team="Golden State Warriors",
                  career_stats="PPG: 23.1 | APG: 6.8 | RPG: 4.4",
                  sport=sport1, user_id=1)
session.add(player2)
session.commit()

player3 = Athlete(
                  name="James Harden", position="Point Guard",
                  team="Houston Rockets",
                  career_stats="PPG: 23.0 | APG: 6.1 | RPG: 5.1",
                  sport=sport1, user_id=1)
session.add(player3)
session.commit()

player4 = Athlete(
                  name="Kevin Durant", position="Small Forward",
                  team="Golden State Warriors",
                  career_stats="PPG: 27.1 | APG: 3.9 | RPG: 7.1",
                  sport=sport1, user_id=1)
session.add(player4)
session.commit()

player5 = Athlete(
                  name="Giannis Antetokounmpo", position="Power Forward",
                  team="Milwaukee Bucks",
                  career_stats="PPG: 17.2 | RPG: 7.5 | BPG: 1.3",
                  sport=sport1, user_id=1)
session.add(player5)
session.commit()

player6 = Athlete(
                  name="Anthony Davis", position="Power Forward",
                  team="New Orleans Pelicans",
                  career_stats="PPG: 23.5 | RPG: 10.3 | BPG: 2.4",
                  sport=sport1, user_id=1)
session.add(player6)
session.commit()

player7 = Athlete(
                  name="Russell Westbrook", position="Point Guard",
                  team="Oklahoma City Thunder",
                  career_stats="PPG: 23.0 | APG: 8.2 | RPG: 6.6",
                  sport=sport1, user_id=1)
session.add(player7)
session.commit()

player8 = Athlete(
                  name="Kawhi Leonard", position="Small Forward",
                  team="Toronto Raptors",
                  career_stats="PPG: 16.4 | APG: 2.3 | RPG: 6.2",
                  sport=sport1, user_id=1)
session.add(player8)
session.commit()

player9 = Athlete(
                  name="Joel Embiid", position="Center",
                  team="Philadelphia 76ers",
                  career_stats="PPG: 22.1 | RPG: 9.9 | BPG: 2.0",
                  sport=sport1, user_id=1)
session.add(player9)
session.commit()

player10 = Athlete(
                   name="Damian Lillard", position="Point Guard",
                   team="Portland Trail Blazers",
                   career_stats="PPG: 23.1 | APG: 6.2 | RPG: 4.1",
                   sport=sport1, user_id=1)
session.add(player10)
session.commit()


# Players for Football
player11 = Athlete(
                   name="Tom Brady", position="Quarterback",
                   team="New England Patriots",
                   career_stats="RAT: 97.6 | YDS: 67,758 | TD: 501",
                   sport=sport2, user_id=1)
session.add(player11)
session.commit()

player12 = Athlete(
                   name="Antonio Brown", position="Wide Receiver",
                   team="Pittsburgh Steelers",
                   career_stats="REC: 773 | YDS: 10,388 | TD: 65",
                   sport=sport2, user_id=1)
session.add(player12)
session.commit()

player13 = Athlete(
                   name="Carson Wentz", position="Quarterback",
                   team="Philadelphia Eagles",
                   career_stats="RAT: 90.8 | YDS: 8,270 | TD: 57",
                   sport=sport2, user_id=1)
session.add(player13)
session.commit()

player14 = Athlete(
                   name="Julio Jones", position="Wide Receiver",
                   team="Atlanta Falcons",
                   career_stats="REC: 629 | YDS: 9,762 | TD: 43",
                   sport=sport2, user_id=1)
session.add(player14)
session.commit()

player15 = Athlete(
                   name="Le'Veon Bell", position="Running Back",
                   team="Pittsburgh Steelers",
                   career_stats="ATT: 1,229 | YDS: 5,336 | TD: 35 ",
                   sport=sport2, user_id=1)
session.add(player15)
session.commit()

player16 = Athlete(
                   name="Todd Gurley", position="Running Back",
                   team="Los Angeles Rams",
                   career_stats="ATT: 915 | YDS: 3,919 | TD: 38",
                   sport=sport2, user_id=1)
session.add(player16)
session.commit()

player17 = Athlete(
                   name="Aaron Donald ", position="Defensive Tackle",
                   team="Los Angeles Rams",
                   career_stats="COMB: 221 | FF: 9 | SACK: 43.0 ",
                   sport=sport2, user_id=1)
session.add(player17)
session.commit()

player18 = Athlete(
                   name="Drew Brees", position="Quarterback",
                   team="New Orleans Saints",
                   career_stats="RAT: 97.3 | YDS: 72,103 | TD: 499",
                   sport=sport2, user_id=1)
session.add(player18)
session.commit()

player19 = Athlete(
                   name="Von Miller", position="Linebacker",
                   team="Denver Broncos",
                   career_stats="COMB: 424 | FF: 25 | INT: 1",
                   sport=sport2, user_id=1)
session.add(player19)
session.commit()

player20 = Athlete(
                   name="Aaron Rodgers", position="Quarterback",
                   team="Green Bay Packers",
                   career_stats="RAT: 103.6 | YDS: 40,499 | TD: 325",
                   sport=sport2, user_id=1)
session.add(player20)
session.commit()


# Players for Soccer
player21 = Athlete(
                   name="Luka Modric", position="Midfielder",
                   team="Real Madrid ",
                   career_stats="GOAL: 27 | AST: 45 | RAT: 7.31",
                   sport=sport3, user_id=1)
session.add(player21)
session.commit()

player22 = Athlete(
                   name="Cristiano Ronaldo", position="Striker",
                   team="Juventus F.C.",
                   career_stats="GOAL: 432 | AST: 121 | RAT: 8.13",
                   sport=sport3, user_id=1)
session.add(player22)
session.commit()

player23 = Athlete(
                   name="Mohamed Salah", position="Forward",
                   team="Liverpool FC",
                   career_stats="GOAL: 93 | AST: 41 | RAT: 7.27",
                   sport=sport3, user_id=1)
session.add(player23)
session.commit()

player24 = Athlete(
                   name="Kevin de Bruyne", position="Midfielder",
                   team="Manchester City",
                   career_stats="GOAL: 56 | AST: 96 | RAT: 7.58",
                   sport=sport3, user_id=1)
session.add(player24)
session.commit()

player25 = Athlete(
                   name="Antoine Griezmann", position="Forward",
                   team="Atletico Madrid",
                   career_stats="GOAL: 158 | AST: 49 | RAT: 7.26",
                   sport=sport3, user_id=1)
session.add(player25)
session.commit()

player26 = Athlete(
                   name="Eden Hazard", position="Forward",
                   team="Chelsea FC",
                   career_stats="GOAL: 122 | AST: 94 | RAT: 7.59",
                   sport=sport3, user_id=1)
session.add(player26)
session.commit()

player27 = Athlete(
                   name="Harry Kane", position="Striker",
                   team="Tottenham Hotspur",
                   career_stats="GOAL: 136 | AST: 22 | RAT: 7.38",
                   sport=sport3, user_id=1)
session.add(player27)
session.commit()

player28 = Athlete(
                   name="Lionel Messi", position="Forward",
                   team="FC Barcelona",
                   career_stats="GOAL: 429 | AST: 153 | RAT: 8.61",
                   sport=sport3, user_id=1)
session.add(player28)
session.commit()

player29 = Athlete(
                   name="Kylian Mbappe", position="Forward",
                   team="Paris Saint-Germain",
                   career_stats="GOAL: 55 | AST: 25 | RAT: 7.36",
                   sport=sport3, user_id=1)
session.add(player29)
session.commit()

player30 = Athlete(
                   name="Raphael Varane", position="Defender",
                   team="Real Madrid",
                   career_stats="GOAL: 7 | AST: 5 | RAT: 6.99",
                   sport=sport3, user_id=1)
session.add(player30)
session.commit()


# Players for Hockey
player31 = Athlete(
                   name="Connor McDavid", position="Center",
                   team="Edmonton Oilers",
                   career_stats="GOAL: 91 | AST: 176 | PTS: 267",
                   sport=sport4, user_id=1)
session.add(player31)
session.commit()

player32 = Athlete(
                   name="Sidney Crosby", position="Center",
                   team="Pittsburgh Penguins",
                   career_stats="GOAL: 411 | AST: 710 | PTS: 1121",
                   sport=sport4, user_id=1)
session.add(player32)
session.commit()

player33 = Athlete(
                   name="Alex Ovechkin", position="Left Wing",
                   team="Washington Capitals",
                   career_stats="GOAL: 613 | AST: 518 | PTS: 1131",
                   sport=sport4, user_id=1)
session.add(player33)
session.commit()

player34 = Athlete(
                   name="Drew Doughty", position="Defender",
                   team="Los Angeles Kings",
                   career_stats="GOAL: 102 | AST: 324 | PTS: 426",
                   sport=sport4, user_id=1)
session.add(player34)
session.commit()

player35 = Athlete(
                   name="Evgeni Malkin", position="Center",
                   team="Pittsburgh Penguins",
                   career_stats="GOAL: 373 | AST: 569 | PTS: 942",
                   sport=sport4, user_id=1)
session.add(player35)
session.commit()

player36 = Athlete(
                   name="Nikita Kucherov", position="Right Wing",
                   team="Tampa Bay Lightning",
                   career_stats="GOAL: 147 | AST: 190 | PTS: 337",
                   sport=sport4, user_id=1)
session.add(player36)
session.commit()

player37 = Athlete(
                   name="Erik Karlsson", position="Defender",
                   team="San Jose Sharks",
                   career_stats="GOAL: 126 | AST: 396 | PTS: 522",
                   sport=sport4, user_id=1)
session.add(player37)
session.commit()

player38 = Athlete(
                   name="Victor Hedman", position="Defender",
                   team="Tampa Bay Lightning",
                   career_stats="GOAL: 83 | AST: 282 | PTS: 365",
                   sport=sport4, user_id=1)
session.add(player38)
session.commit()

player39 = Athlete(
                   name="Anze Kopitar", position="Center",
                   team="Los Angeles Kings",
                   career_stats="GOAL: 292 | AST: 538 | PTS: 830",
                   sport=sport4, user_id=1)
session.add(player39)
session.commit()

player40 = Athlete(
                   name="Taylor Hall", position="Left Wing",
                   team="New Jersey Devils",
                   career_stats="GOAL: 192 | AST: 289 | PTS: 481",
                   sport=sport4, user_id=1)
session.add(player40)
session.commit()


# Players for Baseball
player41 = Athlete(
                   name="Mike Trout", position="Center Field",
                   team="Los Angeles Angels",
                   career_stats="AVG: .307 | HR: 240 | RBI: 648",
                   sport=sport5, user_id=1)
session.add(player41)
session.commit()

player42 = Athlete(
                   name="Clayton Kershaw", position="Left-Hand Pitcher",
                   team="Los Angeles Dodgers",
                   career_stats="ERA: 2.39 | W-L: 153-69 | SO: 2275",
                   sport=sport5, user_id=1)
session.add(player42)
session.commit()

player43 = Athlete(
                   name="Jose Altuve", position="Second Baseman",
                   team="Houston Astros",
                   career_stats="AVG: .316 | HR: 97 | RBI: 464",
                   sport=sport5, user_id=1)
session.add(player43)
session.commit()

player44 = Athlete(
                   name="Max Scherzer", position="Right-Hand Pitcher",
                   team="Washington Nationals",
                   career_stats="ERA: 3.22 | W-L: 159-82 | SO: 2449",
                   sport=sport5, user_id=1)
session.add(player44)
session.commit()

player45 = Athlete(
                   name="Bryce Harper", position="Right Field",
                   team="Washington Nationals",
                   career_stats="AVG: .279 | HR: 184 | RBI: 521",
                   sport=sport5, user_id=1)
session.add(player45)
session.commit()

player46 = Athlete(
                   name="Corey Kluber", position="Right-Hand Pitcher",
                   team="Cleveland Indians",
                   career_stats="ERA: 3.09 | W-L: 96-55 | SO: 1423",
                   sport=sport5, user_id=1)
session.add(player46)
session.commit()

player47 = Athlete(
                   name="Nolan Arenado", position="Third Baseman",
                   team="Colorado Rockies",
                   career_stats="AVG: .291 | HR: 186 | RBI: 616",
                   sport=sport5, user_id=1)
session.add(player47)
session.commit()

player48 = Athlete(
                   name="Chris Sale", position="Left-Hand Pitcher",
                   team="Boston Red Sox",
                   career_stats="ERA: 2.89 | W-L: 103-62 | SO: 1789",
                   sport=sport5, user_id=1)
session.add(player48)
session.commit()

player49 = Athlete(
                   name="Joey Votto", position="First Baseman",
                   team="Cincinnati Reds",
                   career_stats="AVG: .311 | HR: 269 | RBI: 897",
                   sport=sport5, user_id=1)
session.add(player49)
session.commit()

player50 = Athlete(
                   name="Carlos Correa", position="Shortstop",
                   team="Houston Astros",
                   career_stats="AVG: .277 | HR: 81 | RBI: 313",
                   sport=sport5, user_id=1)
session.add(player50)
session.commit()


print ("Added All Sports and Players!")
