from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def page_main():
    if request.method == 'POST':
      return 'You have successfully posted your data!'
    else:
      return render_template('home.html')
#      return 'The form should appear here!'

@app.route('/list/')
def page_list():
    return 'All records should be listed here!'


@app.route('/list/<string:username>/')
def page_list_user(username):
    return 'The record made by the user %s should appear here!' % username
