from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config["APP_NAME"] = "Shopping App"

products = [
    {"id": 1, "name": "T-Shirt", "price": 499},
    {"id": 2, "name": "Shoes", "price": 999},
    {"id": 3, "name": "Bag", "price": 699}
]

cart = []


@app.route("/")
def home():
    return render_template("index.html", products=products, cart=cart)


@app.route("/add/<int:id>")
def add_to_cart(id):
    for product in products:
        if product["id"] == id:
            cart.append(product)

    return redirect(url_for("home"))


@app.route("/remove/<int:index>")
def remove_from_cart(index):
    if 0 <= index < len(cart):
        cart.pop(index)

    return redirect(url_for("home"))


@app.route("/checkout")
def checkout():
    total = sum(item["price"] for item in cart)

    return render_template(
        "checkout.html",
        cart=cart,
        total=total
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(debug=True)