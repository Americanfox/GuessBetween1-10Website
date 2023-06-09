from flask import Flask
from random import randint

number = randint(0, 9)
print(number)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Guess The Number Between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess == number:
       return '<h1 style="color: green;> You Found Me </h1>' \
              '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess > number:
        return '<h1 style="color: red;> Too High, Try Again </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < number:
        return '<h1 style="color: red;> Too Low, Try Again </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'





if __name__ == "__main__":
    app.run(debug=True)