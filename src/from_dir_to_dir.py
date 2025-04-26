import os
import shutil

def copy_from_dir_to_dir(from_dir="static", to_dir="public"):
    if not os.path.exists(from_dir):
        raise Exception(f"Invalid path to {from_dir}")

    if os.path.exists(to_dir):
        shutil.rmtree(to_dir)
    os.mkdir(to_dir)
    

    # COPY
    for item in os.listdir(from_dir):
        item_path_from = os.path.join(from_dir, item)
        item_path_to = os.path.join(to_dir, item)
        if os.path.isfile(item_path_from):
            shutil.copy(item_path_from, item_path_to)
            print(f"Copied file: {item_path_from} to {item_path_to}")
        else:
            os.mkdir(item_path_to)
            copy_from_dir_to_dir(item_path_from, item_path_to)


