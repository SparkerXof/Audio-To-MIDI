# AI-based Audio-to-MIDI converter

Web app based on [Basic Pitch](https://github.com/spotify/basic-pitch) Automatic Music Transcriptor model by Spotify. Uses Flask as frontend and backend.

## Usage
### 1. Docker
```
docker build -t audio-to-midi .
docker run -d -p 5000:5000 audio-to-midi:latest
```
### 2. Python
Python 3.11 recommended as most compatible with all dependencies.
```
python3.11 -m venv venv
source venv/bin/activate
pip3.11 install -r requirement.txt
python3.11 app.py
```
