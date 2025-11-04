from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    return "hello world", 200

@app.route("/LLM", methods=["POST"])
def echo_json():
    data = request.get_json()  # Read JSON from request



    if data.get("bill_type") is None or data.get("document_text") is None:
        return jsonify({"message": "Must pass bill type and document text"}), 400

    print(data["ben"])

    print("Received JSON:", data)  # Just print it to terminal

    return jsonify({
        "message": "Received!",
        "your_data": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
