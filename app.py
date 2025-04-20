from flask import Flask, render_template, request, redirect, url_for
import os
from utils.measure import process_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        output_path = filepath.replace('.', '_out.')
        width, height, area = process_image(filepath, output_path)

        result = {
            'filename': filename,
            'output': os.path.basename(output_path),
            'width': width,
            'height': height,
            'area': area
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)