import os
import sys
import yaml
import logging
from tqdm import tqdm

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Diagnostic prints
print("Current working directory:", os.getcwd())
print("Contents of current directory:", os.listdir())
print("Python path:", sys.path)

if os.path.exists('src'):
    print("Contents of src directory:", os.listdir('src'))
    print("Full path of src directory:", os.path.abspath('src'))
else:
    print("src directory does not exist")

# Now import the required modules
try:
    print("Attempting to import from src.video_to_audio...")
    from src.video_to_audio import process_media
    print("Successfully imported process_media from src.video_to_audio")
    from src.transcription import transcribe_audios
    from src.utils import setup_logging, create_output_directories
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure the file names in the 'src' directory match the import statements.")
    print("Python is looking for modules in these locations:")
    for path in sys.path:
        print(f"  {path}")
    sys.exit(1)

def main():
    try:
        # Load configuration
        with open('config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)

        # Setup logging
        logger = setup_logging(level=logging.INFO)

        # Create output directories
        output_dir = create_output_directories(config['directories']['output'])

        # Process media files
        logger.info(f"Starting media processing from {config['directories']['input']}")
        audio_files = process_media(config['directories']['input'], output_dir)
        print(f"Processed audio files: {audio_files}")
        logger.info(f"Processed audio files: {audio_files}")

        # Check if audio files were processed correctly
        if not audio_files:
            logger.error("No audio files processed. Check if the input directory contains media files.")
            sys.exit(1)

        # Transcribe audio files
        logger.info("Starting audio transcription")
        
        total_files = len(audio_files)
        with tqdm(total=total_files, desc="Overall Progress", unit="file") as pbar:
            def update_progress(future):
                pbar.update()
            
            transcribe_audios(audio_files, output_dir, config['transcription'], update_progress)

        logger.info("Processing complete")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
