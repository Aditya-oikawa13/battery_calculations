from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call the function to initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Here, perform your file processing and calculations
        result = "Result of your calculations"

        # Save result to the database
        conn = sqlite3.connect('results.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO results (result) VALUES (?)", (result,))
        conn.commit()
        conn.close()

        return redirect(url_for('show_results'))

@app.route('/results')
def show_results():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    conn.close()
    return render_template('results.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
