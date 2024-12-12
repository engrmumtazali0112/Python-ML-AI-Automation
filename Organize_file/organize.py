import os
import shutil

# File types for categorization
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.go', '.php']
}

# Function to get file type based on extension
def get_file_category(file_extension):
    for category, extensions in file_types.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'  # Default category if no match

# Function to organize files
def organize_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The specified directory '{directory}' does not exist.")
        return
    
    # Change to the target directory
    os.chdir(directory)

    # List all files in the directory
    files = [f for f in os.listdir() if os.path.isfile(f)]

    if not files:
        print("No files found in the directory.")
        return

    for file in files:
        file_extension = os.path.splitext(file)[1]
        category = get_file_category(file_extension)

        # Create the category directory if it doesn't exist
        if not os.path.exists(category):
            os.makedirs(category)
        
        # Move the file to the category directory
        shutil.move(file, os.path.join(category, file))
        print(f"Moved: {file} to {category}/")

# Main function
if __name__ == "__main__":
    # Provide the path of the directory you want to organize
    directory_path = input("Enter the directory path to organize: ")
    
    # Ensure the path is correct (on Windows, you should use raw string or escape backslashes)
    directory_path = directory_path.strip()  # To remove any leading/trailing spaces

    organize_files(directory_path)
    print("File organization completed.")
