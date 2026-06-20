# Hangman Game 🎮

A simple **Flask-based Hangman game** deployed on Render.  
Play it live 👉 [https://hangman-game-otvc.onrender.com](https://hangman-game-otvc.onrender.com)

---

## 📢 Internship
This project was developed as part of my **CodeAlpha Internship** (Python).

---

## 🚀 Features
- Classic Hangman gameplay
- Random word selection
- Session-based tracking
- Deployed on Render (Free tier)

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Gunicorn
- Render

---

## 🧩 Concepts Used
This project demonstrates key Python concepts:
- **random** → to select a word from a predefined list
- **while loop** → to keep the game running until win/lose
- **if-else** → to check correct vs incorrect guesses
- **strings** → to compare guessed letters with the word
- **lists** → to store guessed letters
- **limit of 6 attempts** → classic Hangman rule

---

## 📂 Project Structure

CodeAlpha_pythonprojects/
│
├── requirements.txt
├── Procfile
└── handman_game/   # (typo, can rename to hangman_game)
└── app.py

2. Install dependencies
bash
pip install -r ../requirements.txt
3. Run locally
bash
python app.py
App will be available at http://127.0.0.1:5000

🌐 Deployment
Hosted on Render

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Root Directory: handman_game
👨‍💻 Author
Hema Teja  
Second-year Computer Science Engineering student
Sir C.R. Reddy College of Engineering
