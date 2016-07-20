from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/game')
def show_madlib_form():
    """Gets user's response...from /game.html"""

    yes_no = request.args.get("yesno")

    if yes_no == "no":
        return render_template("goodbye.html")
    elif yes_no == "yes":
        return render_template("game.html")
    else:
        return "Choose yes or no!"


@app.route('/madlib')
def show_madlib():

    given_person = request.args.get("person")
    given_color = request.args.get("color")
    given_adjective = request.args.get("adjective")
    given_noun = request.args.get("noun")

    return render_template("madlib.html",
                            color=given_color,
                            noun=given_noun,
                            adjective=given_adjective,
                            person=given_person)



@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
