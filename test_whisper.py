import whisper

try:
    model = whisper.load_model("base")
    print("Model loaded successfully")
except AttributeError as e:
    print(f"AttributeError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
