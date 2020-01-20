# [Hood-watch]()
Description
This is an application where a user can sign up and login into a neighborhood where they can post events happening in the neighborhood or post their businesses

### Setup and installations Prerequisites
Python3.6
Postgres
virtualenv
Pip
### Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql
Clone the Repo and checkout into the project folder.
git clone git@github.com:Kaundu/Hood-watch.git && cd Hood-watch
Create and activate the virtual environment
python3.6 -m virtualenv virtual
source virtual/bin/activate
Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:

SECRET_KEY='<Secret_key>'
DBNAME='hood'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

Install dependancies
Install dependancies that will create an environment for the app to run 
`pip install -r requirements.txt`

Create the Database
In a new terminal, open the postgresql shell with psql.

CREATE DATABASE hood;
Make and run migrations
python3.6 manage.py makemigrations && python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open localhost:8000

### Deployment
To deploy the application, please follow the instructions [here](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)

### Contributing
Please read this comprehensive guide on how to contribute. Pull requests are welcome :-)

### Bugs
The app is still in work so posting businesses and viewing the is somewhat of a problem
Support and contact details
Contact Neville Kaundu for further help/support

### License
[MIT](https://github.com/Nyakinyua/Hood/blob/master/LICENSE)

Copyright (c)2020

