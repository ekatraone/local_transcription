import os
import time
import logging

def setup_logging(log_file='app.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory created: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")
    else:
        print(f"Directory already exists: {directory}")

def log_progress(message):
    logging.info(message)
    print(message)

def cooling_period(seconds):
    time.sleep(seconds)


