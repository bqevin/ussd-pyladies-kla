import flask
from pprint import pprint
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to PyLadies Meetup'


@app.route('/callback/ussd', methods=['POST'])
def ussd():
    response = ""

    text_param = request.form.get('text')
    text_list = text_param.split('*')

    # sessionId, phoneNumber, networkCode, serviceCode, text
    # If user just dialed *384#
    if not text_list[0]:
        response = "CON Welcome to PyLadies banking USSD app\n"
        response += "1. See your balance\n"
        response += "2. Transfer money\n"

        # If user selects 1 from 1st menu
    elif text_list[0] == "1":
        response = "END Your balance is: 0/-"
    # If user selects 2 from 1st menu
    elif text_list[0] == "2":
        response = "CON How much do you wanna transfer?"
        pprint(text_list)

    if text_list[0] == "2" and len(text_list) > 1:
        response = "END you have input " + text_list[1]

    return response


app.run()
