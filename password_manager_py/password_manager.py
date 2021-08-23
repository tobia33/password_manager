import os
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import InvalidToken
import Manager
import manager_exceptions
import manager_support
from getpass import getpass

os.system("clear")
partial_welcome_string = "Welcome to Password Manager!"
wrapping_lines = "#"*50 + "\n\t"

how_many_sx = (50 - 10 - len(partial_welcome_string)) // 2
how_many_dx = how_many_sx + len(partial_welcome_string) % 2
welcome_string = "\n\t" + wrapping_lines*3 + "#"*how_many_sx + "-----" +\
    partial_welcome_string + "-----" + "#"*how_many_dx + "\n\t" + wrapping_lines*3
print(welcome_string)

print("-------------------------------------------------------------------------")
print(">most used commands: 'add', 'get', 'delete'\n")
print(">if you write their name preceded by 'h' you will get a mini-explanation,")
print("for example 'hadd', 'hget',... give it a try!\n")
print(">write quit to save the session and quit, clear to clear the terminal\n")
print(">for a list of all commands and their usage just write 'help'")

manager = Manager.Manager("/home/tobia/projects/git_workspace/password_manager/password_manager_py/data")
manager.load_data()
while True:
    print("-------------------------------------------------------------------------")
    command = input("what should I do?\n>")
    if command == "quit" or command == "q":
        manager.write_data()
        break
    if command == "clear" or command == "c":
        os.system("clear")
        continue
    nonExplanation = manager_support.explanationManager(command)
    if nonExplanation:
        decryption_key = None
        if command[:3] == "add" or command[0] == "a"or command[:3] == "get"\
                or command[0] == "g":
            decryption_key = input("write the decryption key you want to use\n")
        elif command[:6] == "delete":
            decryption_key = getpass("write the decryption key needed to decrypt this password\n")
        try:
            manager = manager_support.executeCommand(manager, command, decryption_key)
        except Exception as e:
            if isinstance(e, manager_exceptions.GroupNotFoundException):
                print("\nthe given group is invalid, try changing it!\n")
                continue
            elif isinstance(e, manager_exceptions.KeyNotFoundException):
                print("\nthe given key is invalid, try changing it!\n")
                continue
            elif isinstance(e, manager_exceptions.CommandNotFoundException):
                print("\nthe given command is invalid, try changing it!\n")
                continue
            elif isinstance(e, ValueError):
                print("\nthe decryption_key is invalid, try another one please\n")
                continue
            elif isinstance(e, InvalidSignature):
                print("\nthe decryption_key is wrong, try again and change it!\n")
                continue
            elif isinstance(e, InvalidToken):
                print("\nthe decryption_key is wrong, try again and change it!\n")
                continue
            else:
                save = input("an error has occurred, do you want to save before interrupting?\n\t(y/n)")
                if save != "n" and save != "no":
                    manager.write_data()
                raise e
