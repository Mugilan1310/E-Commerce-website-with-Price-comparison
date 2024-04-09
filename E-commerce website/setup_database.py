# setup_database.py

import pyodbc

def connect_db():
    # Change the connection string based on your Access database file path
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\E-commerce website\online mobile shop.accdb;'
    return pyodbc.connect(connection_string)

def setup_database():
    db = connect_db()

    # Create products table if not exists
    db.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id AUTOINCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            price FLOAT NOT NULL,
            image TEXT NOT NULL
        )
    ''')

    # Insert sample data if the table is empty
    cursor = db.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        db.execute("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", ('iPhone X', 999.99, 'iphone.jpg'))
        db.execute("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", ('Samsung Galaxy S21', 799.99, 'samsung.jpg'))

        db.commit()
        print("Sample data inserted.")
    else:
        print("Data already exists in the database.")

    db.close()

if __name__ == '__main__':
    setup_database()
