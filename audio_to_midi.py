from basic_pitch.inference import Model
from basic_pitch import ICASSP_2022_MODEL_PATH
from basic_pitch.inference import run_inference
from basic_pitch.note_creation import model_output_to_notes

def generate_midi_from_audio(audio, model, onset_thr=0.5, frame_thr=0.3):
    output = run_inference(audio_path=audio, model_or_model_path=model)
    midi_data, note_event = model_output_to_notes(output, onset_thresh=onset_thr, frame_thresh=frame_thr)

    return midi_data

if __name__ == "__main__":
    model = Model(ICASSP_2022_MODEL_PATH)
    generate_midi_from_audio(audio="testaudio/heartbreaking.mp3", model=model)