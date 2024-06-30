# Video to Audio Transcription Project

## Overview
This project automates the process of converting video files to audio and then transcribing the audio content. It's designed to handle large batches of videos efficiently, with built-in cooling periods to prevent system overload.

## Features
- Converts video files to MP3 audio format
- Transcribes audio to text using OpenAI's Whisper model
- Processes videos in batches with multi-threading
- Implements cooling periods for system stability
- Provides progress updates and time estimates
- Configurable settings via a configuration file
- Logging support for debugging and record-keeping
- Optional GPU acceleration for faster transcription

## Dependencies
- Python 3.7+
- ffmpeg-python
- openai-whisper
- pyyaml
- torch (for GPU acceleration)

## Project Structure
```
video-to-audio-transcription/
│
├── src/
│   ├── __init__.py
│   ├── video_to_audio.py
│   ├── transcription.py
│   └── utils.py
│
├── config.yaml
├── main.py
├── requirements.txt
├── README.md
└── run_colab.ipynb
```

## Usage
1. Update the `config.yaml` file with your desired settings.
2. Run `main.py` to start the transcription process.
3. The script will process all video files in the specified input directory, convert them to audio, transcribe the audio, and save the results in the output directory.

## Output
- Audio files (.mp3) in the `audios` subdirectory of the output folder
- Transcription text files (.txt) in the `transcripts` subdirectory of the output folder
- A log file (`transcription.log`) in the project root directory

## Performance
The script is optimized for batch processing and uses multi-threading to improve performance. It also includes cooling periods to prevent system overheating during long processing sessions. GPU acceleration can be enabled for faster transcription if a compatible CUDA device is available.

For detailed instructions on how to set up and run the project, please refer to the INSTRUCTIONS.md file.
