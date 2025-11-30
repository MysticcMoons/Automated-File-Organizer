import imghdr
import os
import shutil


folder = "#path"



# loop through every file in folder
for file in os.listdir(folder):
    full_path = os.path.join(folder,file)
    

    #Check directory and print then skip
    if os.path.isdir(full_path):
        print("This is a Directory")
        continue

    file_type =  imghdr.what(full_path)

    if file_type is not None:
        print("File Type: " + file_type)

    else:
        print("File Type is Unknown")
    # fullPath = "f{folder}/{file}"  f makes it so we can enter our variables {folder} and {file} in a string




    if file_type is not None:
        _, ext = os.path.splitext(file)
        file_type= ext.lower().lstrip(".") or "unknown"


        # create a folder if it doesnt exist
        dest_folder = os.path.join(folder, file_type)
        os.makedirs(dest_folder, exist_ok = True)
        
        dest_path = os.path.join(dest_folder, file)
        print(f"Moving {file} -> {dest_folder}")
        shutil.move(full_path, dest_path)


