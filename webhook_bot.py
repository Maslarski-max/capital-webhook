
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'ZDvSs2mkRmAt9D7h'
CAPITAL_API_URL = "https://api-capital.backend-capital.com"

def place_order(action, symbol, qty):
    side = "BUY" if action == "buy" else "SELL"
    headers = {
        "X-CAP-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "market": symbol,
        "direction": side,
        "size": qty,
        "orderType": "MARKET"
    }
    r = requests.post(f"{CAPITAL_API_URL}/api/v1/orders", headers=headers, json=data)
    return r.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action = data.get("action")
    symbol = data.get("symbol")
    qty = data.get("qty")

    result = place_order(action, symbol, qty)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
