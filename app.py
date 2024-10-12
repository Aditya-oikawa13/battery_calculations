from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)

# Set a folder to store the uploaded files (you can change this)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected'
    
    # Save the file to the upload folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    # Process the file (for now, just reading it with pandas)
    df = pd.read_excel(filepath)  # Assuming Excel file
    
    # Example: Sum the first column (this is just a placeholder for actual logic)
    result = df.iloc[:, 0].sum()
    
    return f'The sum of the first column is: {result}'

if __name__ == '__main__':
    app.run(debug=True)

