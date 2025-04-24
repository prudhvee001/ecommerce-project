from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/recommend/<int:product_id>", methods=["GET"])
def recommend(product_id):
    with open("recommendations.json") as f:
        data = json.load(f)

    suggestions = data.get(str(product_id), [])
    return jsonify({
        "product_id": product_id,
        "recommendations": suggestions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)
