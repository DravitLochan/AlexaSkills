import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)


@ask.intent("YesIntent")

def next_round():

	'''FirstPhrase = ['half ', 'quarter',
			  '1 minute ', '2 minute ', '3 minute ', '4 minute ', '5 minute '
			  '6 minute ', '7 minute ', '8 minute ', '9 minute ', '10 minute ',
			  '11 minute ', '12 minute ', '13 minute ', '14 minute ', '15 minute ',
			  '16 minute ', '17 minute ', '18 minute ', '19 minute ', '20 minute ',
			  '21 minute ', '22 minute ', '23 minute ', '24 minute ', '25 minute ',
			  '26 minute ', '27 minute ', '28 minute ', '29 minute ', '30 minute ',
			  '31 minute ', '32 minute ', '33 minute ', '34 minute ', '35 minute ',
			  '36 minute ', '37 minute ', '38 minute ', '39 minute ', '40 minute ',
			  '41 minute ', '42 minute ', '43 minute ', '44 minute ', '45 minute ',
			  '46 minute ', '47 minute ', '48 minute ', '49 minute ', '50 minute ',
			  '51 minute ', '52 minute ', '53 minute ', '54 minute ', '55 minute ',
			  '56 minute ', '57 minute ', '58 minute ', '59 minute ' ]'''
	option = randint(0, 2);					# 0 -> half; 1 -> quarter; 2 -> number
	if option == 0 :
		firstPhrase = 'half'
	elif option == 1 :
		firstPhrase = 'quarter'
	else:
		minutes = str(randint(1, 59))
		firstPhrase = minutes + ' minutes '

	option = randint(0, 1)
	if option == 0 :
		secondPhrase = 'to '
	else:
		secondPhrase = 'past '

	hour = str(randint(1, 12))
	finalPhrase = firstPhrase + secondPhrase + hour

	round_msg = render_template('round', phrase=finalPhrase)

	session.attributes['firstPhrase'] = firstPhrase
	session.attributes['secondPhrase'] = secondPhrase
	session.attributes['hour'] = hour

	return question(round_msg)


if __name__ == '__main__':

    app.run(debug=True)