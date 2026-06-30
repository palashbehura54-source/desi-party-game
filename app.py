import os
from flask import Flask, render_template, request, jsonify
import random

# Import your static data banks
from data.safe_bank import safe_bank
from data.spicy_bank import spicy_bank
from data.shots_bank import shots_bank
from data.panga_bank import panga_bank

app = Flask(__name__)

# Game Memory
game_state = {
    "players": [],
    "player_stats": {},
    "current_player": None,
    "total_turns_taken": 0,
    "spicy_threshold": 12
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/add_player', methods=['POST'])
def add_player():
    data = request.json
    name = data.get('name')
    if name and name not in game_state["players"]:
        game_state["players"].append(name)
        game_state["player_stats"][name] = {"truth": 0, "dare": 0}
    return jsonify({"players": game_state["players"]})


@app.route('/api/spin_bottle', methods=['GET'])
def spin_bottle():
    if not game_state["players"]:
        return jsonify({"error": "No players"})

    selected = random.choice(game_state["players"])
    game_state["current_player"] = selected
    stats = game_state["player_stats"][selected]

    return jsonify({
        "selected_player": selected,
        "stats": stats
    })


@app.route('/api/get_prompt', methods=['POST'])
def get_prompt():
    data = request.json
    choice_type = data.get('type')
    current_player = game_state["current_player"]

    if choice_type in ['truth', 'dare']:
        game_state["player_stats"][current_player][choice_type] += 1

    game_state["total_turns_taken"] += 1
    is_spicy_mode = game_state["total_turns_taken"] > game_state["spicy_threshold"]

    opponent_name = ""

    if choice_type == 'panga':
        prompt = random.choice(panga_bank)
        mode_label = "PANGA (1v1)"
        possible_opponents = [p for p in game_state["players"] if p != current_player]
        if possible_opponents:
            opponent_name = random.choice(possible_opponents)

    elif choice_type == 'shot':
        prompt = random.choice(shots_bank)
        mode_label = "DRINK"

    else:
        active_bank = spicy_bank if is_spicy_mode else safe_bank
        prompt = random.choice(active_bank[choice_type])
        mode_label = f"18+ {choice_type.upper()}" if is_spicy_mode else choice_type.upper()

    return jsonify({
        "prompt": prompt,
        "mode_label": mode_label,
        "opponent": opponent_name,
        "is_spicy": is_spicy_mode
    })


if __name__ == '__main__':
    # Cloud servers use dynamic ports, this ensures it works locally and on Render
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)