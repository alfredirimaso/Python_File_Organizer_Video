
import os
import shutil

# 1. Choose the folder you want to organize
folder_path = r"C:\Users\alisoft\Documents"

# 2. Define file categories and their extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Programs": [".exe", ".msi", ".py", ".java", ".apk"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# 3. Check whether the folder exists
if not os.path.isdir(folder_path):
    print("Error: The folder does not exist!")
else:
    # 4. Read all items in the selected folder
    for filename in os.listdir(folder_path):

        # Build the full path to the item
        source = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(source):
            continue

        # Get the file extension
        extension = os.path.splitext(filename)[1].lower()

        # Assume the file is of an unknown type
        category = "Others"

        # Find the correct category
        for folder, extensions in file_types.items():
            if extension in extensions:
                category = folder
                break

        # Create the category folder if necessary
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        # Build the destination file path
        destination = os.path.join(destination_folder, filename)

        # Avoid overwriting files with the same name
        if os.path.exists(destination):
            print(f"Skipped duplicate: {filename}")
            continue

        # Move the file into its category
        shutil.move(source, destination)

        print(f"Moved {filename} -> {category}")

    print("\nFolder organization completed!")
