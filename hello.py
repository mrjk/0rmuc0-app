from flask import Flask
app = Flask(__name__)

@app.route('/')
def page_main():
    return 'The form should appear here!'

@app.route('/list')
def page_list():
    return 'All records should be listed here!'


@app.route('/list/<string:username>')
def page_list_user(username):
    return 'The record made by the user %s should appear here!' % username
