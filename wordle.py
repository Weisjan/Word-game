from flask import Flask, session, render_template, request, redirect, url_for
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
MAX_ATTEMPTS = 6

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        guess = request.form['guess'].lower()
        if len(guess) != 5:
            return render_template('index.html', error="Please enter a 5-letter word.", attempts=session['attempts'], remaining_attempts=session['remaining_attempts'])
        result = []
        for i in range(5):
            if guess[i] == session['word'][i]:
                result.append((guess[i], 'green'))
            elif guess[i] in session['word']:
                result.append((guess[i], 'yellow'))
            else:
                result.append((guess[i], 'red'))
        session['attempts'].append(result)
        session['remaining_attempts'] = MAX_ATTEMPTS - len(session['attempts'])
        if guess == session['word']:
            return redirect(url_for('game_over'))
        elif session['remaining_attempts'] <= 0:
            return redirect(url_for('game_over_loose'))
        else:
            return render_template('index.html', attempts=session['attempts'], remaining_attempts=session['remaining_attempts'])
    else:
        if 'attempts' not in session or 'word' not in session:
            session.clear()
            session['word'] = choice(words).lower()
            session['attempts'] = []
            session['remaining_attempts'] = MAX_ATTEMPTS
            print(session['word'])
        return render_template('index.html', attempts=session['attempts'], remaining_attempts=session['remaining_attempts'])

@app.route("/gameover", methods=["GET", "POST"])
def game_over():
    if request.method == "POST":
        session.clear()
        return redirect(url_for('home'))
    else:
        return render_template('win.html', word=session['word'])

@app.route("/gameover_loose", methods=["GET", "POST"])
def game_over_loose():
    if request.method == "POST":
        session.clear()
        return redirect(url_for('home'))
    else:
        return render_template('loose.html', word=session['word'])

if __name__ == "__main__":
    with open("words_eng.txt", 'r') as file:
        words = [line.strip() for line in file.readlines() if len(line.strip()) == 5]
    app.run(debug=True)
