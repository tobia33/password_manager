import os
import Manager
import manager_exceptions
import manager_support
from getpass import getpass

print("Welcome to Password Manager!")
print("choose the data file you want to work with\n")
os.system("ls")
data_file = input()
manager = Manager.Manager(data_file)
manager.load_data()
while True:
    print("-----------------------------------------------------------------------")
    print("most used commands: add, get, undo, print_all")
    print("if you write their name you will get a mini-explanation, give it a try!")
    print("for a list of all commands and their usage just write help")
    command = input()
    nonExplanation = manager_support.explanationManager(command)
    if nonExplanation:
        decryption_key = None
        if command[:3] == "add" or command[:3] == "get":
            decryption_key1 = getpass("write the decryption key you want to use")
            decryption_key2 = getpass("write it again please")
            if decryption_key1 != decryption_key2:
                raise manager_exceptions.WrongDecryptionKeyException("the decryption \
                keys are different!")
            decryption_key = decryption_key1
        try:
            manager = manager_support.executeCommand(manager, command, decryption_key)
        except manager_exceptions.GroupNotFoundException("the given group is invalid,\
         try changing it!\n"):
            input("press ENTER to continue")
            continue
        except manager_exceptions.KeyNotFoundException("the given key is invalid,\
         try changing it!\n"):
            input("press ENTER to continue")
            continue
        except manager_exceptions.CommandNotFoundException("the given command is invalid,\
         try changing it!\n"):
            input("press ENTER to continue")
            continue
        print("operation completed successfully!")
    continue

#TODO fai lo scambio in byte nel encript e decript