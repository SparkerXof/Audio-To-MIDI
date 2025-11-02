from basic_pitch.inference import predict

def generate_midi_from_audio(audio, model):
    model_output, midi_data, note_event = predict(audio_path=audio, model_or_model_path=model)

    return midi_data
