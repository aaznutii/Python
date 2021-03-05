import os

interface = int(input("Choose your mode:\n 1.Console mode\n 2.Easy mode\n ??? "))
if interface == 2:
    command = 'python core.py'
    os.system(command)
elif interface == 1:
    command = 'python console_mode.py'
    os.system(command)
else:
    print("Bye!")
