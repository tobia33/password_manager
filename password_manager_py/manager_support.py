from PyQt5.QtCore import dec
from cryptography.fernet import Fernet
import manager_exceptions
"------------------------------cryptography------------------------------"


def encrypt(value, decryption_key):
    """ encrypt the value using the decryption key """
    decryption_key = fernet_compatible(decryption_key)
    fernet = Fernet(str.encode(decryption_key))
    return fernet.encrypt(str.encode(value)).decode()

def fernet_compatible(decryption_key):
    """ modify the password making it fernet compatible """
    while len(decryption_key) < 43:
        decryption_key += decryption_key
    decryption_key = decryption_key.replace("'", "a")
    decryption_key = decryption_key.replace("`", "b")
    decryption_key = decryption_key.replace(" ", "c")
    return decryption_key[:43] + '='


def decrypt(value, decryption_key):
    """ decrypt the value using the decryption key """
    decryption_key = fernet_compatible(decryption_key)
    fernet = Fernet(str.encode(decryption_key))
    return fernet.decrypt(str.encode(value)).decode()


"------------------------------documentation------------------------------"


def addExpl():
    """ return the explanation of the command add """
    return "\tsyntax: add group key value\n" + \
           "\tadd value in the specified group and with the specified key\n" + \
           "\tthe value is encrypted using the decryption_key asked via prompt\n" \
           "\tthe decryption key is what you will use to access this password again" \
           "\tif you forget it you will not be able to access to your encrypted password ever again\n" \
           "\tif the decryption_key is False the value will not be encrypted\n\n"


def getExpl():
    """ return the explanation of the command get """
    return "\tsyntax: get group key\n" + \
           "\tget the value of the specified group of the specified key\n" + \
           "\tthe value is decrypted using the decryption_key asked via prompt\n" +\
           "\tif the decryption_key is False the value will not be decrypted\n\n"


def delExpl():
    """ return the explanation of the command delete """
    return "\tsyntax: delete group key\n" + \
           "\tdelete the specified key of the specified group\n" +\
           "\tyou need to insert the correct decryption key you used to encrypt the password\n\n"


def undoExpl():
    """ return the explanation of the command undo """
    return "\tsyntax: undo\n\tundo the latest change\n\n"


def redoExpl():
    """ return the explanation of the command redo """
    return "\tsyntax: redo\n\tredo the latest change\n\n"


def printAllExpl():
    """ return the explanation of the command print_all """
    return "\tsyntax: print_all\n\tprint all the data available\n\n"


def printGroupExpl():
    """ return the explanation of the command print_group """
    return "\tsyntax: print_group group\n" + \
           "\tprint the data of the specified group\n\n"


def resetExpl():
    """ return the explanation of the command reset """
    return "\tsyntax: reset\n\treset the session\n\n"


def helpExpl():
    """ return the explanation of all the commands """
    return "add:\n" + addExpl() + \
           "get:\n" + getExpl() + \
           "delete:\n" + delExpl() + \
           "undo:\n" + undoExpl() + \
           "redo:\n" + redoExpl() + \
           "print_all:\n" + printAllExpl() + \
           "print_group:\n" + printGroupExpl() + \
           "reset:\n" + resetExpl()


def explanationManager(command):
    """ manages the explanations for the commands """
    if command == "hadd":
        print(addExpl())
    elif command == "hget":
        print(getExpl())
    elif command == "hdelete":
        print(delExpl())
    elif command == "hundo":
        print(undoExpl())
    elif command == "hredo":
        print(redoExpl())
    elif command == "hprint_all":
        print(printAllExpl())
    elif command == "hprint_group":
        print(printGroupExpl())
    elif command == "hreset":
        print(resetExpl())
    elif command == "help":
        print(helpExpl())
    else:
        return True


"------------------------------execute command------------------------------"


def executeCommand(manager, command):
    """ recognize the command and execute it """
    if command == "undo":
        manager.undo()
        return manager
    elif command == "redo":
        manager.redo()
        return manager
    elif command == "reset":
        manager.reset_session()
        return manager
    elif command == "print_all" or command == "p":
        print(manager.all__data_string())
        return manager
    opcode, *addressing_mode = command.split()
    if opcode == "print_group" or opcode == "pg":
        print(manager.group_data_string(addressing_mode[0]))
        return manager
    elif opcode == "add" or opcode == "a":
        decryption_key = "first"
        while decryption_key == "first" or decryption_key == "h" or decryption_key == "help":
            decryption_key = input("what decryption key do you want to use?\n"
                               ">if you don't know what I'm asking for write 'h' or 'help'\n"
                               ">if you want to go back write 'b' or 'back'")
            if decryption_key == "b" or decryption_key == "back":
                return manager
            elif decryption_key == "help" or decryption_key == "h":
                print(addExpl())
        manager.add(addressing_mode[0], addressing_mode[1], addressing_mode[2], decryption_key)
        return manager
    manager.check_group(addressing_mode[0])
    manager.check_key(addressing_mode[1])
    if opcode == "get" or opcode == "g":
        decryption_key = "first"
        while decryption_key == "first" or decryption_key == "h" or decryption_key == "help":
            decryption_key = input("what decryption key do you want to use?\n"
                               ">if you don't know what I'm asking for write 'h' or 'help'\n"
                               ">if you want to go back write 'b' or 'back'")
            if decryption_key == "b" or decryption_key == "back":
                return manager
            elif decryption_key == "help" or decryption_key == "h":
                print(getExpl())
        print("\n" + manager.get(addressing_mode[0], addressing_mode[1], decryption_key))
        return manager
    elif opcode == "delete" or opcode == "d":
        decryption_key = "first"
        while decryption_key == "first" or decryption_key == "h" or decryption_key == "help":
            decryption_key = input("what decryption key do you want to use?\n"
                                   ">if you don't know what I'm asking for write 'h' or 'help'\n"
                                   ">if you want to go back write 'b' or 'back'")
            if decryption_key == "b" or decryption_key == "back":
                return manager
            elif decryption_key == "help" or decryption_key == "h":
                print(delExpl())
            manager.delete(addressing_mode[0], addressing_mode[1], decryption_key)
            return manager
    else:
        raise manager_exceptions.CommandNotFoundException
