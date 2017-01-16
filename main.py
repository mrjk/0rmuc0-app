#!/usr/bin/python


# Initialisation
############################
from flask import Flask
from flask import render_template, g, request, flash
import sqlite3
import os

# Instanciate application
app = Flask(__name__)

# Define settings from another file
app.config.from_object(__name__) # load config from this file , flaskr.py


# Application settings
############################

# Settings - for dev
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '0rmuc0.db'),
    SECRET_KEY='this-is-my-devlopment-key',
    USERNAME='admin',
    PASSWORD='admin'
))

app.config.from_envvar('ORMUCO_DEBUG', silent=True)


# App - Routing
############################
@app.route('/', methods=['GET', 'POST'])
def page_main():

    # Build template array
    args = {}
    args["page_title"] = "Add new entry"
    args["flash_type"] = "success"

    # If POST, then add data to the DB
    db = get_db()
    if request.method == 'POST':

      # Check if user is already registered
      cur = db.execute('select username from user_data where username=?', [ request.form['username']])
      if len( cur.fetchall() ) > 0:
        flash('Failed: You already registerd data with your username %s' % ( request.form["username"]))
        args["flash_type"] = "danger"
      else:
        db.execute('insert into user_data (username, color, pet) values (?, ?, ?)',
          [request.form['username'], request.form['color'], request.form['pet']]
        )
        db.commit()
        flash('Success: New entry added for user %s (favorite color is %s and prefered pet is %s)' % ( request.form["username"], request.form["color"], request.form["pet"]))

    # Get a db dump
    cur = db.execute('select username, color, pet from user_data order by id desc')

    # Display template
    args["records"] = cur.fetchall()
    return render_template('home.html', args=args)


@app.route('/list/')
def page_list():
    db = get_db()
    cur = db.execute('select username, color, pet from user_data order by id desc')

    args = {}
    args["page_title"] = "Records listing"
    args["records"] = cur.fetchall()

    return render_template('list.html', args=args)


@app.route('/list/<string:username>/')
def page_list_user(username=None):

    args = {}
    args["page_title"] = "Data of user " + str(username)
    args["username"] = username

    return render_template('list_user.html', args=args)


# App - Internal
############################
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# App - CLI
############################
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


# Functions
############################
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    """This allows to initialise the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# vim: ts=4 sw=4 et

### v##im##: ##tabstop=4 expandtab shiftwidth=2 softtabstop=2


