from flask import Flask, render_template, request

import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    target = random.randint(1, 100)
    turns = 10
    score = 0
    message = "guess the number between 1 to 100"

    while turns > 0:
        guess = int(request.form.get('guess'))

        if target < guess:
            message = "Too High"
        elif target > guess:
            message = "Too Low"
        else:
            message = "Correct"
            score += 1
            break

        turns -= 1

    return render_template('index.html', message=message, score=score)

if __name__ == '__main__':
    app.run()