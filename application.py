from flask import Flask
application = Flask(__name__)
@application.route('/')
def health_check():
    return 'App running healthy'