from flask import Flask, render_template, request
import random
import re
from datetime import datetime
import webbrowser
import threading

app = Flask(__name__)

# Rule-based intents
intents = {
    "hello": ["Hi there! 👋", "Hello!", "Hey, nice to see you!"],
    "how are you": ["I'm doing great, thanks!", "Feeling awesome today!", "I'm fine, how about you?"],
    "bye": ["Goodbye! 👋", "See you later!", "Take care!"],
    "time": [lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}"],
    "date": [lambda: f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"],
    "joke": ["Why don’t programmers like nature? Too many bugs 🐛",
             "I told my computer a joke, but it didn’t get it 🤖"],
    "quote": ["Believe in yourself 💪", "Keep pushing forward 🚀", "Success is built on consistency 🔑"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, replies in intents.items():
        if re.search(pattern, user_input):
            reply = random.choice(replies)
            return reply() if callable(reply) else reply
    return "Hmm 🤔 I don’t know that yet. Try asking for time, date, joke, or quote!"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = get_response(user_input)
    return {"reply": response}

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
