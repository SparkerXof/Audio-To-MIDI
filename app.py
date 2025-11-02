import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from basic_pitch.inference import Model
from basic_pitch import ICASSP_2022_MODEL_PATH
from audio_to_midi import generate_midi_from_audio

ALLOWED_EXTENSIONS = {'mp3', 'ogg', 'wav', 'flac', 'm4a'}

model = Model(ICASSP_2022_MODEL_PATH)

app = Flask(__name__)
app.config['TEMP_FOLDER'] = '/tmp'

def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'audioFile' not in request.files:
            return render_template('index.html', error="No file uploaded")
        file = request.files['audioFile']
        if file.filename == '':
            return render_template('index.html', error="File doesn't exits")
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            temp_audi_path = os.path.join(app.config['TEMP_FOLDER'], filename)
            temp_midi_path = os.path.join(app.config['TEMP_FOLDER'], filename.split('.')[0] + ".mid")
            file.save(temp_audi_path)
            midi_file = generate_midi_from_audio(temp_audi_path, model)
            midi_file.write(temp_midi_path)
            return send_file(temp_midi_path)
        else:
            return render_template('index.html', error="Wrong file extension")
    return render_template('index.html', error="")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
