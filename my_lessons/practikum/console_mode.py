import func
import sys
import os

print("Enetering console mode through CMD")
print("For the list of console commands type 'help'")
os.startfile('c:\windows\system32\cmd')

command2 = sys.argv[1]

if command2 == "help":
    print("create_file (name) (data) - create file (name) with (data)")
    print("create_folder (name) - create_folder")
    print("get_list - get list of files and folders")
    print("get_folders - get list of folders")
    print("copy (name) (new_name) - copy file (name) to file (new_name)")
    print("del - delete file or folder")
    print("ch_dir /path - changes working directory")
    print("game1 - game 'Guess the number'")
    print("game2 - game 'Guess the number reversed'")

elif command2 == "create_file":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Missing file name")
    else:
        data = sys.argv[3]
        func.create_file(name, data)
        func.logger(f"Created file: {name} with data: {data}")
elif command2 == "create_folder":
    try:
        name = sys.argv[2]
    except IndexError:
        print("Missing folder name")
    else:
        func.create_folder(name)
        func.logger(f"Created folder: {name}")
elif command2 == "get_list":
    func.get_list(False)
    func.logger("Got file list")
elif command2 == "get_folders":
    func.get_list(True)
    func.logger("Got folder list")
elif command2 == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Missing file name")
    try:
        new_name = sys.argv[4]
    except IndexError:
        print("Missing new file name")
    else:
        func.copy_files(name, new_name)
        func.logger(f"Copied file(folder): {name} to file(folder): {new_name}")
elif command2 == 'del':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Missing file name")
    else:
        func.del_files(name)
        func.logger(f"Deleted file(folder): {name}")
elif command2 == "ch_dir":
    name = sys.argv[2]
    func.ch_dir(name)
    print(os.getcwd())
elif command2 == "game1":
    print("Game 'Guess the number'")
    command3 = 'python ../Guess_the_number_for_money.py'
    os.system(command3)
elif command2 == "game2":
    print("Game 'Guess the number Reversed'")
    command3 = 'python ../Comp_guesses_your_number.py'
    os.system(command3)
