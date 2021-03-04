import os
import sys


def create_dir():
    name = sys.platform
    module_path = os.getcwd()
    for i in range(1, 4):
        new_dir = os.path.join(module_path, f'{name}_{i}')
        os.mkdir(new_dir)


def del_dir():
    name = sys.platform
    module_path = os.getcwd()
    for i in range(1, 4):
        new_dir = os.path.join(module_path, f'{name}_{i}')
        os.rmdir(new_dir)
