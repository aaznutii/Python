"""
Практическое задание
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
(на уроке разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной из игр:
“угадай число” или “угадай число (наоборот)”.
"""
import func
import os

print("Main menu:\n1.Create file\n2.Create folder\n3.Get list\n4.Copy\n5.Delete\n6.Change dir\n7"
      ".Game 'Guess the number'\n8.Game 'Guess the number Reversed'")
choice = int(input("Choose an option: "))
if choice == 1:
    name = input("File name: ")
    data = input("Input data: ")
    func.create_file(name, data)
    func.logger(f"Created file: {name} with data: {data}")
elif choice == 2:
    name = input("Folder name: ")
    func.create_folder(name)
    func.logger(f"Created folder: {name}")
elif choice == 3:
    fold_only = None
    while fold_only != "y" and fold_only != "n":
        fold_only = input("Folders only? (y/n): ")
        if fold_only == "y":
            func.get_list(True)
            func.logger("Got folder list")
        elif fold_only == "n":
            func.get_list(False)
            func.logger("Got file list")
        else:
            print("Try again!")
elif choice == 4:
    name = input("File name: ")
    new_name = input("New file name: ")
    func.copy_files(name, new_name)
    func.logger(f"Copied file(folder): {name} to file(folder): {new_name}")
elif choice == 5:
    name = input("Delete file(folder) with name: ")
    func.del_files(name)
    func.logger(f"Deleted file(folder): {name}")
elif choice == 6:
    name = input("Input path: ")
    func.ch_dir(name)
elif choice == 7:
    print("Game 'Guess the number'")
    command3 = 'python ../Guess_the_number_for_money.py'
    os.system(command3)
elif choice == 8:
    print("Game 'Guess the number Reversed'")
    command3 = 'python ../Comp_guesses_your_number.py'
    os.system(command3)
else:
    print("Bye!")
