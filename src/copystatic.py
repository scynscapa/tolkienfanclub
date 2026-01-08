import os
import shutil

def copy_static():
    destination = "docs"
    static = "static"

    if os.path.exists(destination):
        shutil.rmtree(destination)
    else:
        raise FileNotFoundError(f"Directory : {destination} does not exist")
    
    os.mkdir(destination)
    copy_directory_contents(static, destination)
    

def copy_directory_contents(src_dir, dest_dir):
    static_list = os.listdir(src_dir)

    for file in static_list:
        path = os.path.join(src_dir, file)
        dest_path = os.path.join(dest_dir, file)

        if os.path.isfile(path):
            shutil.copy(path, dest_dir)
        elif os.path.isdir(path):
            os.mkdir(dest_path)
            copy_directory_contents(path, dest_path)
        