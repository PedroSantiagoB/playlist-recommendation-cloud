from flask import Flask, request, jsonify
import pickle
from datetime import datetime

app = Flask(__name__)

model_path = "../mnt/data/association_rules.pickle"
app.model = pickle.load(open(model_path, "rb"))
app.model_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def recommend_songs(user_songs, rules):
    recommended_songs = set()
    for rule in rules:
        if set(rule[0]).issubset(user_songs):
            recommended_songs.update(rule[1])
    return list(recommended_songs)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json(force=True)
        user_songs = data.get("songs", [])

        if not user_songs:
            return jsonify({
                "error": "Invalid input. 'songs' field is required and must not be empty."
            }), 400

        recommendations = recommend_songs(set(user_songs), app.model)

        response = {
            "songs": recommendations,
            "version": "1.0",
            "model_date": app.model_date,
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=52054)
