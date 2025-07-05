from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_mysql_user',
        password='your_password',
        database='portfolio'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT filename, caption FROM photos")
    photos = cursor.fetchall()
    conn.close()
    return render_template('gallery.html', photos=photos)

@app.route('/about')
def about():
    return render_template('about.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
