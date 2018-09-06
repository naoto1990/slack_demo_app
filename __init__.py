from flask import Flask, request, Response, jsonify
import os
import json

from slash_calc.addon.calculator import Calculator
from slash_calc.addon.parser import Parser

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

            response = {
                "text": input_text,
                "attachments": [
                    {
                        "text":""
                    }
                ]
            }

            try:
                result = eval(input_text)
                response["attachments"][0]["text"] = "= " + str(result)

                return Response(json.dumps(response), mimetype='application/json')

            except SyntaxError:
                return 'Give me proper request please!'

            except ZeroDivisionError:
                return 'You can not devide by 0!'

    return app
