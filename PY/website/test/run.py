from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World2!'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
@app.route('/projects/')
def projects():
    return 'The project/ page'

@app.route('/about')
def about():
    return 'The about page'
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.2')
