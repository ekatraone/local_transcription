import whisper
import torch

def load_whisper_model(model_name="base"):
    # Load Whisper model 
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    model = whisper.load_model(model_name, device=device)
    return model

def transcribe_audio(model, audio_path):
    # Transcribe audio
    result = model.transcribe(audio_path)
    return result['text']


