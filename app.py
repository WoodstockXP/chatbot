from flask import Flask, request, jsonify, render_template
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/blog")
def blog():
    return render_template("blog.html")


@app.get("/blog-details")
def blog_details():
    return render_template("blog-details.html")


@app.get("/shop")
def shop():
    return render_template("shop.html")


@app.get("/shop-details")
def shop_details():
    return render_template("shop-details.html")


@app.get("/cart")
def shopping_cart():
    return render_template("shopping-cart.html")


@app.get("/checkout")
def checkout():
    return render_template("checkout.html")


@app.get("/contact")
def contact():
    return render_template("contact.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)