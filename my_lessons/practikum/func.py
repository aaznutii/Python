import os
import shutil
import datetime


def create_file(name, data=None):
    with open(name, "w", encoding="utf-8") as fl:
        if data:
            fl.write(data)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Folder already exists!")


def get_list(folders=False):
    result = os.listdir()
    print([i for i in result if os.path.isdir(i)]) if folders else print(result)


def copy_files(name, new_name):
    try:
        shutil.copytree(name, new_name) if os.path.isdir(name) else shutil.copy(name, new_name)
    except FileExistsError:
        print("Folder already exists!")


def del_files(name):
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)


def logger(data):
    current_time = datetime.datetime.now()
    with open("log.md", "a", encoding="utf-8") as f:
        f.write(f"{current_time} - {data}\n")


def ch_dir(name):
    os.chdir(name)
