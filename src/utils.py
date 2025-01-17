import os

def ensure_directory_exists(directory):
    """Ensure that the specified directory exists, create it if not."""
    if not os.path.exists(directory):
        os.makedirs(directory)
