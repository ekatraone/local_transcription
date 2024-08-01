import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"

def extract_audio_from_video(video_path, audio_path):
    print(f"Extracting audio from {video_path} and saving to {audio_path}.")
    
    # Check if the video file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"The video file {video_path} does not exist.")
    
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract audio and save it as a WAV file temporarily
    temp_audio_path = audio_path.replace('.mp3', '.wav')
    video.audio.write_audiofile(temp_audio_path, codec='pcm_s16le')
    
    print('Converting the WAV file to MP3') 
    # Convert the WAV file to MP3
    audio = AudioSegment.from_wav(temp_audio_path)
    audio.export(audio_path, format="mp3", codec="libmp3lame")
    print('Converted the WAV file to MP3')
    
    # Remove the temporary WAV file
    os.remove(temp_audio_path)
    print('Removed the wav file')
    
    print(f"Audio extraction and conversion complete: {audio_path}")


