import os
# import dotenv
from flask import Flask, request, jsonify

# from addon import Calculator

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/multiply', methods=['POST'])
    def multiply():
        if request.method == 'POST':
            if request.form['token'] == verification_token:
                payload = {'text': 'DigitalOcean Slack slash command is successful!'}

                # calculator = Calculator()
                # result = calculator.multiply()

            return jsonify(payload)
    return app
