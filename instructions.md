# Instructions for Running the Video to Audio Transcription Project

## Prerequisites
- Python 3.7 or higher
- FFmpeg installed on your system
- pip (Python package manager)

## Setup

1. Clone or download the project repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Edit the `config.yaml` file to set your input and output directories, and adjust other settings as needed.

## Running the Script

### On Windows and macOS

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Activate the virtual environment (if you haven't already).

4. Run the script:
   ```
   python main.py
   ```

5. The script will process the videos and provide progress updates. Check the `transcription.log` file for detailed logs.

### On Google Colab

1. Upload all project files to your Google Drive.

2. Open the `run_colab.ipynb` notebook in Google Colab.

3. Run the cells in the notebook to set up the environment and process your videos.

## Notes

- Ensure you have sufficient disk space for the audio files and transcripts.
- The script uses the "base" model of Whisper by default. For better accuracy (at the cost of increased processing time), you can change the `model` setting in `config.yaml` to `"medium"` or `"large"`.
- Adjust the `batch_size` and `max_workers` parameters in `config.yaml` to optimize performance for your system.
- To enable GPU acceleration, set `use_gpu: true` in the `config.yaml` file. Make sure you have a CUDA-compatible GPU and the necessary CUDA toolkit installed.
