import os
# import dotenv
from flask import Flask, request, jsonify

from slack_demo.addon.calculator import Calculator
from slack_demo.addon.parser import Parser

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    @app.route('/calc', methods=['POST'])
    def calc():
        if request.method == 'POST' and request.form['token'] == verification_token:
            input_text = request.form['text']

            try:
                result = eval(input_text)
                return str(result)

            except SyntaxError:
                return 'Give me proper request please!'

            except ZeroDivisionError:
                return 'You can not devide by 0!'

    return app
