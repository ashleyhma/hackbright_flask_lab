"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    wants_to_play = request.args.get("wants_to_play")
    print(wants_to_play)
    if wants_to_play == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    person = request.args.get("person").capitalize()
    color = request.args.get("color").capitalize()
    noun = request.args.get("noun").capitalize()
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    verb2 = request.args.get("verb")
    print(verb)
    print(verb2)
    print(request.args)
    # print(request.form)
    # print(request.args.get())
    # print(list(request.args.values()))
    # for value in request.args:
    #     print(value)
    print(request.args.getlist("verb"))
    return render_template("madlib.html",
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            verb=verb)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
