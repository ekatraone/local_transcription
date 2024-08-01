import os
import yaml
from src.video_to_audio import extract_audio_from_video
from src.transcription import load_whisper_model, transcribe_audio
from src.utils import setup_logging, create_dir_if_not_exists, log_progress, cooling_period

# Load configuration
with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

path = config['directories']['path']
path1 = config['directories']['path1']
path2 = config['directories']['path2']
batch_size = config['settings']['batch_size']
cooling_time = config['settings']['cooling_time']

setup_logging()
create_dir_if_not_exists(path)

model = load_whisper_model()

video_files = [f for f in os.listdir(path) if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
print(f"Found {len(video_files)} video files.")

for i in range(0, len(video_files), batch_size):
        batch_files = video_files[i:i + batch_size]
        
        for video_file in batch_files:
            video_path = os.path.join(path, video_file)
            audio_file_name = os.path.splitext(video_file)[0] + '.mp3'
            audio_path = os.path.join(path1, audio_file_name)
            
            log_progress(f"Processing {video_file}...")
            extract_audio_from_video(video_path, audio_path)
            log_progress(f"Audio saved to {audio_path}")

            transcription_file_name = os.path.splitext(video_file)[0] + '.txt'
            transcription_path = os.path.join(path2, transcription_file_name)
            
            log_progress(f"Transcribing audio from {audio_path}...")
            transcription = transcribe_audio(model, audio_path)
            with open(transcription_path, 'w') as f:
                f.write(transcription)
            log_progress(f"Transcription saved to {transcription_path}")

        log_progress("Batch processing complete.")
        cooling_period(cooling_time)
