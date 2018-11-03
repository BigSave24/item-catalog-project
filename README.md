Item Catalog Project
--------------------
Top Flight Sports Catalog Web Application


Purpose
-----------------------
The Top Flight Sports Catalog is a web application that uses Python, Flask, PostgreSQL, Alchemy, HTML, and CSS to manage a catalog of user-created athletes in five major sports categories.


## Requirements
----------------
The following software is needed to run this project:

- [Python 2](https://www.python.org/download/releases/2.7.2/)
- [Flask](http://flask.pocoo.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [OAuth 2.0](https://oauth.net/2/)
- [Vagrant Tool](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)


## Running The Top Flight Sports Catalog Web Application
--------------------------------------------------------
### Project Files
   - `catalog-project.py` Python web application server file
   - `Vagrantfile` Configuration file
   - `database_setup.py` Create *sportscatalog.db* database file
   - `sportsData.py` Data file to populate *sportscatalog.db* database
   - `templates folder` Folder housing HTML templates
   - `static folder` Folder housing CSS and images
   - `README.md` README documentation

### Open a terminal window
Linux\Mac - Use the default terminal application.

Windows - You can use a terminal application such as
[Git Bash](https://gitforwindows.org/) or [Ubuntu](https://www.howtogeek.com/265900/everything-you-can-do-with-windows-10s-new-bash-shell/).  

### Start the VM using Vagrant
Use Vagrant to startup the virtual machine.

##### COMMAND: `vagrant up`

**_\*NOTE\*_** The initial start up may take longer than normal due to the Vagrant managed virtual machine setup process.

### Access the VM using ssh via Vagrant
Log into the virtual machine using ssh.

##### COMMAND: `vagrant ssh`

### Navigate to the *Catalog* directory
After accessing the virtual machine, navigate to the */vagrant/catalog/* directory.

##### COMMAND: `cd /vagrant`

### Create the catalog database file
Create the database file by running the *database_setup.py* file.

##### COMMAND: `python database_setup.py`

### Populate the database with data
Populate the database file with sports and athlete data by running the *sportsData.py* file.

##### COMMAND: `python sportsData.py`

### Run the Top Flight Sports Catalog web app
Run the Top Flight Sports Catalog web application server using Python 2.

##### COMMAND: `python catalog-project.py`

### Access Top Flight Sports Catalog web app
Open a browser and navigate to http://localhost:8000 or http://127.0.0.1:8000 to begin using the application.

### Stop the Top Flight Sports Catalog web app
Stop the Top Flight Sports Catalog web application by running the stop command.

##### COMMAND: `ctrl + c  OR COMMAND + C`

### Shut down and exit the VM
Once completed, you can exit the virtual machine.

##### COMMAND: `exit`

Shut down the virtual machine after logging out.

##### COMMAND: `vagrant halt`
