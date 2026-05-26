from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/", methods=["GET"])
def home():
    return "PAWAN DHAN BOT RUNNING"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("ALERT RECEIVED:")
    print(data)

    action = data.get("action")

    if action == "BUY":
        print("BUY ORDER EXECUTED")

    elif action == "SELL":
        print("SELL ORDER EXECUTED")

    return jsonify({
        "status":"success"
    })

app.run(host="0.0.0.0", port=5000)
