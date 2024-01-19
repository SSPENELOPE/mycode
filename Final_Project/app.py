from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def clear_console():
    # Clear console based on the platform
    # This is a simple console clearing function, which may not work in all environments
    pass


def save_score(username, score):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{username}: {score}\n")


def show_scoreboard():
    with open("scoreboard.txt", "r") as file:
        scoreboard = file.read()
    return scoreboard


def welcome():
    return "Welcome to movie quote trivia. You will be shown quotes from movies and you will be able to pick from 4 options and guess which one it is. Your score will be the total number of movies you guessed correctly"


@app.route("/")
def index():
    return render_template("index.html", welcome_message=welcome())


@app.route("/game", methods=["POST", "GET"])
def game():
    if request.method == "POST":
        username = request.form["username"]
        return redirect("/play?username=" + username)
    return render_template("game.html")


@app.route("/play")
def play():
    username = request.args.get("username")

    questionsAndAnswers = {
        "Stop looking at me Swan!": {
            "A": "Billy Madison",
            "B": "Happy Gilmore",
            "C": "Just Go With It",
            "D": "50 first dates",
        },
        "Why, Johnny Ringo, you look like somebody just walked over your grave.": {
            "A": "3:10 to Yuma",
            "B": "Django",
            "C": "Tombstone",
            "D": "True Grit",
        },
        "Thats not a knife, Thats a knife!": {
            "A": "A bugs life",
            "B": "Crocodile  Dundee",
            "C": "Anaconda",
            "D": "Terminator 2",
        },
        "Hello. My name is Inigo Montoya. You killed my father. Prepare to die.": {
            "A": "The Mask of Zorro",
            "B": "The Princess Bride",
            "C": "The Hunger Games",
            "D": "Demolition Man",
        },
        "I Have To Go See About A Girl.": {
            "A": "Stand by me",
            "B": "The Other Guys",
            "C": "Good Will Hunting",
            "D": "Cast Away",
        },
        "Honey? Where's my super suit!": {
            "A": "Man of Steel",
            "B": "Justice League",
            "C": "Avengers",
            "D": "Incredibles",
        },
        "Heathcote. You know, you remind me of the pilsbury doughboy. If I poke your stomach, will it make you go oh-hoh-hoh-hoh!": {
            "A": "Bulletproof",
            "B": "Major Payne",
            "C": "White Chicks",
            "D": "Scary Movie",
        },
    }

    answerList = ["A", "C", "B", "B", "C", "D", "B"]

    correct_answers = 0
    current_question = 0

    if "current_question" in request.args:
        current_question = int(request.args["current_question"])

    if current_question < len(questionsAndAnswers):
        if "user_answer" in request.args:
            user_answer = request.args["user_answer"].upper()
            correct_answer = answerList[current_question]
            print(f"User answer: {user_answer}")
            print(f"Correct Answer: {correct_answer}")
            print(f"{correct_answers}")

            if user_answer == correct_answer:
                correct_answers += 1

        clear_console()
        question, options = list(questionsAndAnswers.items())[current_question]
        return render_template(
            "play.html",
            username=username,
            question=question,
            options=options,
            current_question=current_question,
        )

    result_message = f"You got {correct_answers} out of {len(questionsAndAnswers)} questions correct."
    save_name = request.args.get("save", "n")

    if save_name.lower() == "y":
        save_score(username, correct_answers)

    show_scoreboard_option = request.args.get("show_scoreboard", "n")
    if show_scoreboard_option.lower() == "y":
        scoreboard = show_scoreboard()
        return render_template(
            "result.html", result=result_message, scoreboard=scoreboard
        )

    return render_template("result.html", result=result_message)


if __name__ == "__main__":
    app.run(debug=True)