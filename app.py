from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home/Landing page
@app.route('/')
def index():
    return render_template('index.html', title="Home | Artisan Handcrafts")

# Route for the Products page
@app.route('/products')
def products():
    # Mock data for products with working placeholder images
    items = [
        {"id": 1, "name": "Ceramic Vases", "price": "$45.00", "image": "https://placehold.co/400x300/a3958c/ffffff?text=Ceramic+Vase", "desc": "Hand-thrown ceramic vases with earthy glazes."},
        {"id": 2, "name": "Woven Baskets", "price": "$30.00", "image": "https://placehold.co/400x300/7A8977/ffffff?text=Woven+Basket", "desc": "Natural seagrass baskets, perfect for storage."},
        {"id": 3, "name": "Linen Scarves", "price": "$55.00", "image": "https://placehold.co/400x300/8C5E58/ffffff?text=Linen+Scarf", "desc": "Soft, organic linen scarves in pastel tones."},
        {"id": 4, "name": "Wooden Bowls", "price": "$28.00", "image": "https://placehold.co/400x300/cbb8a3/2d2d2d?text=Wooden+Bowl", "desc": "Carved from reclaimed oak, finished with beeswax."},
        {"id": 5, "name": "Candle Set", "price": "$22.00", "image": "https://placehold.co/400x300/dccfc6/2d2d2d?text=Soy+Candles", "desc": "Hand-poured soy wax candles with essential oils."}
    ]
    return render_template('products.html', title="Our Collection | Artisan Handcrafts", products=items)

# Route for the About page
@app.route('/about')
def about():
    return render_template('base.html', title="Our Story | Artisan Handcrafts") 

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('base.html', title="Contact Us | Artisan Handcrafts")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
