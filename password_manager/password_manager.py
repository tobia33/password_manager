import os

import cryptography.exceptions

import Manager
import manager_exceptions
import manager_support
from getpass import getpass

print("Welcome to Password Manager!")
print("choose the data file you want to work with\n")
manager = Manager.Manager("/home/tobia/projects/git_workspace/password_manager/password_manager/data")
manager.load_data()
while True:
    print("-------------------------------------------------------------------------")
    print(">most used commands: 'add', 'get', 'delete'")
    print(">if you write their name preceded by 'h' you will get a mini-explanation,")
    print("for example 'hadd', 'hget',... give it a try!")
    print(">for a list of all commands and their usage just write 'help'")
    print(">write quit to save the session and quit, clear to clear the terminal\n")
    command = input()
    if command == "quit":
        manager.write_data()
        break
    if command == "clear":
        os.system("clear")
        continue
    nonExplanation = manager_support.explanationManager(command)
    if nonExplanation:
        decryption_key = None
        if command[:3] == "add":
            decryption_key = input("write the decryption key you want to use\n")
        elif command[:3] == "get":
            decryption_key = getpass("write the decryption key you want to use\n")
        elif command[:6] == "delete":
            decryption_key = getpass("write the decryption key needed to decrypt this password\n")
        try:
            manager = manager_support.executeCommand(manager, command, decryption_key)
        except Exception as e:
            if isinstance(e, manager_exceptions.GroupNotFoundException):
                print("\nthe given group is invalid, try changing it!\n")
                input("press ENTER to continue")
                continue
            elif isinstance(e, manager_exceptions.KeyNotFoundException):
                print("\nthe given key is invalid, try changing it!\n")
                input("press ENTER to continue")
                continue
            elif isinstance(e, manager_exceptions.CommandNotFoundException):
                print("\nthe given command is invalid, try changing it!\n")
                input("press ENTER to continue")
                continue
            elif isinstance(e, ValueError):
                print("\nthe decryption_key is invalid, try another one please\n")
                input("press ENTER to continue")
                continue
            elif isinstance(e, cryptography.exceptions.InvalidSignature):
                print("\nthe decryption_key is wrong, try again and change it!\n")
                input("press ENTER to continue")
                continue
            elif isinstance(e, cryptography.fernet.InvalidToken):
                print("\nthe decryption_key is wrong, try again and change it!\n")
                input("press ENTER to continue")
                continue
            else:
                raise e.with_traceback()
    print("\noperation completed successfully!\n")
