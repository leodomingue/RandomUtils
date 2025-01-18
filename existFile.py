import os

def check_file_exists(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.isfile(file_path)
