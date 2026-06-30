# Desi Night 🎉 - The Ultimate Party Game

A fast-paced, web-based digital Truth or Dare party game designed specifically for a group of guys hanging out. Built with a "Desi" touch, featuring competitive 1v1 'Panga' challenges, drinking rules, an automatic 18+ mode escalation, and a native iOS app feel.
Live at: https://desi-party-game.onrender.com

**Made by Palash ❤️**

---

## ✨ Features

*   **📱 Native App Feel:** Add to your iOS or Android home screen for a full-screen, immersive UI with zero browser bars.
*   **🍾 Spin the Bottle:** A fast-paced roulette animation picks the next victim randomly. No one knows whose turn is next!
*   **🔥 Escalation Engine:** The game starts tame but automatically switches to Spicy (18+) mode after 12 total turns.
*   **⚖️ Built-in Limits:** Players can only choose 3 Truths and 3 Dares per game. After that, they are forced to take a Shot or pick a Panga (1v1).
*   **⚔️ Panga Mode:** Head-to-head competitive 1v1 challenges (roast battles, push-up contests, trivia).
*   **🛠️ Admin Controls:** The host can instantly add, kick individual players, or wipe the whole lobby with the 'Clear All' button.

---

## 📁 Project Structure

```text
desi-party-game/
├── requirements.txt      # Python dependencies (Flask, Gunicorn)
├── app.py                # Main Flask backend & logic engine
├── README.md             # You are here
├── data/
│   ├── __init__.py       # Makes the data folder a module
│   ├── safe_bank.py      # Early-game Desi comedy questions
│   ├── spicy_bank.py     # 18+ drama, texts, and secrets
│   ├── shots_bank.py     # Drinking rules
│   └── panga_bank.py     # Competitive 1v1 challenges
└── templates/
    └── index.html        # Frontend UI, CSS animations, and JS logic
