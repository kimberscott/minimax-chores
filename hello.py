from flask import (
    Flask,
    url_for,
    render_template,
    request,
    session,
    redirect,
)
from markupsafe import escape
from dotenv import load_dotenv
import os

load_dotenv()



app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv('SECRET_KEY') #b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/greet/<name>")
def greet(name):
    return f"Greetings, {escape(name)}!"

# Run as: flask --app hello run
# To make visible within network: flask --app hello run --host=0.0.0.0
# Add --debug for debug mode: reloads with code changes and launches browser debugger on errors

@app.get('/login_alt')
def login_get():
    return 'show the login form'

@app.post('/login_alt')
def login_post():
    return 'do the login'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('sample.html', name=name)

@app.route('/')
def index():
    if 'username' in session:
        app.logger.debug(f'user: {session["username"]}')
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        app.logger.debug(f'user: {session["username"]}')
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

with app.test_request_context():
    print(url_for('hello_world', next='/'))
    print(url_for('greet', name='John Doe'))
    print(url_for('static', filename='style.css'))

# *cookies(accessible on request, set on response)
# *sessions
# return redirect(url_for('login'))
#
# abort(401)
# this_is_never_executed()
#
# flash messages
#