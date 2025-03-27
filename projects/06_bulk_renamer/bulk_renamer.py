import os

def bulk_rename_files(folder_path, prefix="file_", replace_word=None, new_extension=None):
    try:
        if not os.path.exists(folder_path):
            print("❌ Error: Folder does not exist. Please enter a valid path.")
            return
        
        files = os.listdir(folder_path)
        
        count = 1

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(file_path):
                continue

            file_extension = os.path.splitext(file_name)[1]

            if replace_word and replace_word in file_name:
                new_name = file_name.replace(replace_word, prefix)
            else:
                new_name = f"{prefix}{count}{file_extension}"  

            if new_extension:
                new_name = os.path.splitext(new_name)[0] + new_extension

            new_file_path = os.path.join(folder_path, new_name)

            os.rename(file_path, new_file_path)
            print(f"✅ Renamed: {file_name} → {new_name}")

            count += 1  

    except Exception as e:
        print(f"❌ Error: {e}")

folder = input("Enter folder path: ")
prefix = input("Enter file prefix (default is 'file_'): ") or "file_"
replace_word = input("Enter a word to replace in filenames (or press Enter to skip): ") or None
new_extension = input("Enter new file extension (e.g., .jpg, .txt) or press Enter to keep original: ") or None

bulk_rename_files(folder, prefix, replace_word, new_extension)
