from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
import os
from signature_extractor import extract_signature
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.secret_key = 'supersecretkey'  # Needed for flash messages

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            # Extract signature
            result_filename = f"extracted_{os.path.splitext(filename)[0]}.png"
            result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
            extract_signature(upload_path, result_path)
            return render_template('index.html', result_file=result_filename, uploaded_file=filename)
        else:
            flash('Invalid file type')
            return redirect(request.url)
    return render_template('index.html', result_file=None, uploaded_file=None)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
