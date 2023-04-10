import os
import datetime
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    action = request.form.get('action')
    folder_name = request.form.get('foldername')
    if not folder_name:
        return "Please enter a folder name"
    if 'file' not in request.files:
        return "No file part"
    files = request.files.getlist('file')
    if not files:
        return "No selected file"
    # Add date and time stamp to the folder name
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d%Y_%H%M")
    user_folder = os.path.join('/code', f'{folder_name}_{timestamp}')
    # Create a subdirectory for the user's files
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    for file in files:
        file.save(os.path.join(user_folder, file.filename))
    # Save the entered previous companies in a dict file in the user's subdirectory
    previous_companies = request.form.get('prev_companies')
    if previous_companies:
        with open(os.path.join(user_folder, 'dict'), 'w') as f:
            f.write(previous_companies)
    if action == 'file_import':
        os.system(f'./file_import.sh {folder_name}')
        return "Files uploaded successfully"
    elif action == 'code_import':
        os.system(f'./import_code {folder_name}')
        return "Code uploaded successfully"
    elif action == 'files_and_code_import':
        os.system(f'./files_plus_code_import.sh {folder_name}')
        return "Files and code uploaded successfully"
    elif action == 'search_metadata':
        # Call file_metadata.sh with folder name and timestamp
        os.system(f'./file_metadata.sh {folder_name} {timestamp}')
        return "File metadata search initiated"
    else:
        return "Invalid action"

@app.route('/upload_status')
def upload_status():
    return render_template('upload_status.html')

# @app.route('/download_metadata')
# def download_metadata():
#     metadata_file = os.path.join(app.config['UPLOAD_FOLDER'], 'metadata.csv')
#     return send_file(metadata_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
