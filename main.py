from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def page_main():
#    if request.method == 'POST':
    return render_template('home.html', arg_method=request.method)

@app.route('/list/')
def page_list():
    return 'All records should be listed here!'


@app.route('/list/<string:username>/')
def page_list_user(username=None):
    return render_template('list_user.html', arg_username=username)
