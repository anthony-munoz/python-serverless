
from app.flask_factory import app
from app.router import configure_api

configure_api(app)


if __name__ == '__main__':
    app.run(debug=True)



#Other way to do this thing
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#   return 'Hello, World!'

# if __name__ == '__main__':
#   app.run()