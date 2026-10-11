import os
import shutil

folder_to_organize = "Test_Folder"
list_of_files = os.listdir(folder_to_organize)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    # We added 'extension != ".py"' so it doesn't move our own code file
    if extension != "" and not name.startswith(".") and extension != ".py":
        
        # This removes the first character (the dot) from the extension
        # So '.pdf' becomes 'pdf'
        folder_name = extension[1:] 
        
        # This creates a path like: Test_Folder/pdf
        folder_path = os.path.join(folder_to_organize, folder_name)
        
        # If this folder doesn't exist yet, Python will create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Define the current location of the file, and its new destination
        current_location = os.path.join(folder_to_organize, file_name)
        new_location = os.path.join(folder_path, file_name)
        
        # The command that physically moves the file
        shutil.move(current_location, new_location)
        
        print(f"Successfully moved {file_name} to the {folder_name} folder!")