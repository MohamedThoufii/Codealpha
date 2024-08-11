import os
import shutil
import tempfile

# Define file type categories and their respective file extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx", ".xlsx", ".xls"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".php"]
}

def create_folders(directory, categories):
    for category in categories.keys():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(directory, categories):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    moved = True
                    break
            if not moved:
                # If the file does not match any category, move it to 'Others' folder
                others_folder = os.path.join(directory, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

def simulate_file_creation(directory):
    """Simulate the creation of files for testing."""
    sample_files = {
        "image1.jpg": "Images",
        "document1.pdf": "Documents",
        "video1.mp4": "Videos",
        "music1.mp3": "Music",
        "archive1.zip": "Archives",
        "script1.py": "Scripts",
        "misc.txt": "Others"
    }
    
    for filename, category in sample_files.items():
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write("This is a sample file for testing.")
        print(f"Created {file_path} in {category}")

if __name__ == "__main__":
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as directory_to_organize:
        print(f"Organizing files in temporary directory: {directory_to_organize}")

        # Simulate file creation
        simulate_file_creation(directory_to_organize)
        
        # Create folders and organize files
        create_folders(directory_to_organize, file_categories)
        organize_files(directory_to_organize, file_categories)
        
        print("Files organized successfully.")
