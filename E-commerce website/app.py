from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'], check_same_thread=False)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    cursor = g.db.execute('SELECT * FROM products')
    products = cursor.fetchall()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    cursor = g.db.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
