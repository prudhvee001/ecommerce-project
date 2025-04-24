from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def read_cart():
    with open('cart.json') as f:
        return json.load(f)

@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    carts = read_cart()
    for cart in carts:
        if cart['user_id'] == user_id:
            return jsonify(cart)
    return jsonify({"message": "Cart not found"}), 404

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    carts = read_cart()
    user_cart = next((c for c in carts if c['user_id'] == data['user_id']), None)

    if user_cart:
        user_cart['items'].append({
            "product_id": data['product_id'],
            "quantity": data['quantity']
        })
    else:
        carts.append({
            "user_id": data['user_id'],
            "items": [{
                "product_id": data['product_id'],
                "quantity": data['quantity']
            }]
        })

    with open('cart.json', 'w') as f:
        json.dump(carts, f, indent=2)
    return jsonify({"message": "Item added to cart"})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003)
