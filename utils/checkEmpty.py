import os

def check_empty_files_and_folders(dir_path) -> None:
    ...:     for root, dirnames, files in os.walk(dir_path, topdown=False):
    ...:         for f in files:
    ...:             full_name = os.path.join(root, f)
    ...:             if os.path.getsize(full_name) == 0:
    ...:                 os.path.basename(full_name)
    ...:
    ...:         for dirname in dirnames:
    ...:             full_path = os.path.realpath(os.path.join(root, dirname))
    ...:             if not os.listdir(full_path):
    ...:                 os.listdir(full_path)
