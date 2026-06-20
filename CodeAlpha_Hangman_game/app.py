from flask import Flask, request, session, redirect, url_for
import random, os, webbrowser

app = Flask(__name__)
app.secret_key = os.urandom(24)

WORDS = ["python", "flask", "hangman", "developer", "internship", "colorful", "emoji"]

# ASCII Hangman stages
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nickname = request.form["nickname"]
        session["nickname"] = nickname
        session.pop("word", None)  # reset game state
        return redirect(url_for("game"))
    return """
    <h1>🎮 Welcome to Hangman!</h1>
    <form method="POST">
        Nickname: <input type="text" name="nickname" required><br>
        <button type="submit">Start Game</button>
    </form>
    """

@app.route("/game", methods=["GET", "POST"])
def game():
    if "nickname" not in session:
        return redirect(url_for("home"))

    if "word" not in session:
        session["word"] = random.choice(WORDS)
        session["guesses"] = []
        session["attempts"] = 6
        session["message"] = "🎮 Guess wisely… 🌈"
        session["shake"] = False
        session["win"] = False
        session["game_over"] = False

    if request.method == "POST":
        guess = request.form["guess"].lower()
        if guess and guess not in session["guesses"]:
            session["guesses"].append(guess)
            if guess not in session["word"]:
                session["attempts"] -= 1
                session["shake"] = True
            else:
                session["shake"] = False

        if all(letter in session["guesses"] for letter in session["word"]):
            session["message"] = "🎉 Woohoo! You cracked the code! 🏆"
            session["win"] = True
            session["game_over"] = True
        elif session["attempts"] <= 0:
            session["message"] = f"💀 Oops! Game over… The word was 👉 {session['word']}"
            session["game_over"] = True

    display_word = " ".join([letter if letter in session["guesses"] else "_" for letter in session["word"]])
    shake_class = "shake" if session.get("shake") else ""
    confetti_script = """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>confetti();</script>
    """ if session.get("win") else ""

    ascii_stage = HANGMAN_PICS[6 - session["attempts"]]

    # Full-screen popup overlay if game over
    overlay = ""
    if session.get("game_over"):
        overlay = f"""
        <div id="overlay">
            <div class="overlay-content">
                <h2>{session['message']}</h2>
                <a href="{url_for('reset')}" class="btn">🔄 Play Again</a>
                <a href="{url_for('home')}" class="btn exit">❌ Exit</a>
            </div>
        </div>
        <style>
            #overlay {{
                position: fixed; top:0; left:0; width:100%; height:100%;
                background: rgba(0,0,0,0.85); color:white;
                display:flex; align-items:center; justify-content:center;
                z-index:9999;
            }}
            .overlay-content {{
                text-align:center; background:#222; padding:30px; border-radius:15px;
            }}
            .btn {{
                display:inline-block; margin:10px; padding:10px 20px;
                background:#4caf50; color:white; border-radius:8px; text-decoration:none;
            }}
            .btn.exit {{ background:#f44336; }}
        </style>
        """

    return f"""
    <html>
    <head>
        <title>🌈 Hangman Game 🎮</title>
        <style>
            body {{ background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a6c1ee); font-family:'Comic Sans MS'; text-align:center; }}
            h1 {{ font-size:3em; color:#fff; text-shadow:2px 2px #000; }}
            .word {{ font-size:2em; letter-spacing:10px; background:#fff; padding:10px; border-radius:10px; display:inline-block; }}
            .message {{ font-size:1.5em; background:#ffe066; padding:15px; border-radius:10px; display:inline-block; }}
            .shake {{ animation: shake 0.5s; }}
            @keyframes shake {{ 25%{{transform:translateX(-5px)}}50%{{transform:translateX(5px)}}75%{{transform:translateX(-5px)}} }}
            .reset {{ background:#4caf50; padding:10px 20px; color:white; border-radius:8px; text-decoration:none; }}
            pre {{ font-size:1.2em; color:white; }}
        </style>
    </head>
    <body>
        <h1>🌈 Hangman Challenge 🎮</h1>
        <p>Player: {session['nickname']}</p>
        <div class="word {shake_class}">{display_word}</div>
        <pre>{ascii_stage}</pre>
        <div class="message">{session['message']}</div>
        <p>Attempts left: ❤️ {session['attempts']}</p>
        <form method="POST">
            <input type="text" name="guess" maxlength="1" required>
            <button type="submit">✨ Guess</button>
        </form>
        <br>
        <a href="{url_for('reset')}" class="reset">🔄 New Game</a>
        {confetti_script}
        {overlay}
    </body>
    </html>
    """

@app.route("/reset")
def reset():
    if "nickname" not in session:
        return redirect(url_for("home"))
    session.pop("word", None)
    return redirect(url_for("game"))

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    webbrowser.open(url)   # auto‑opens browser
    app.run(debug=True)
