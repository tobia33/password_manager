from cryptography.fernet import Fernet
import manager_exceptions

"------------------------------cryptography------------------------------"
def encript(value, decryption_key):
    """ encript the value using the decryption key """
    fernet = Fernet(decryption_key)
    return fernet.encrypt(value)

def decript(value, decryption_key):
    """ decript the value using the  t=decryption key """
    fernet = Fernet(decryption_key)
    return fernet.decrypt(value)

"------------------------------documentation------------------------------"

def addExpl():
    """ return the explanation of the command add """
    return "\tsyntax: add group key value\n" +\
           "\tadd value in the specified group and with the specified key\n" +\
           "\tthe value is encrypted using the decryption_key asked via prompt\n\n"

def getExpl():
    """ return the explanation of the command get """
    return "\tsyntax: get group key\n" +\
           "\tget the value of the specified group of the specified key\n" +\
           "\tthe value is decrypted using the decryption_key asked via prompt\n\n"

def delExpl():
    """ return the explanation of the command delete """
    return "\tsyntax: delete group [key]\n" + \
           "\tdelete the specified group or, if present, the specified key\n\n"

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
    return "\tsyntax: print_group group\n" +\
           "\tprint the data of the specified group\n\n"

def resetExpl():
    """ return the explanation of the command reset """
    return "\tsyntax: reset\n\treset the session\n\n"

def helpExpl():
    """ return the explanation of all the commands """
    return "add:\n" + addExpl() +\
           "get:\n" + getExpl() +\
           "delete:\n" + delExpl() +\
           "undo:\n" + undoExpl() +\
           "redo:\n" + redoExpl() +\
           "print_all:\n" + printAllExpl() +\
           "print_group:\n" + printGroupExpl() +\
           "reset:\n" + resetExpl()

def explanationManager(command):
    if command == "add":
        print(addExpl())
    elif command == "get":
        print(getExpl())
    elif command == "delete":
        print(delExpl())
    elif command == "undo":
        print(undoExpl())
    elif command == "redo":
        print(redoExpl())
    elif command == "print_all":
        print(printAllExpl())
    elif command == "print_group":
        print(printGroupExpl())
    elif command == "reset":
        print(resetExpl())
    elif command == "help":
        print(helpExpl())
    else:
        return True

"------------------------------execute command------------------------------"


def executeCommand(manager, command, decryption_key):
    if command == "undo":
        return manager.undo()
    elif command == "redo":
        return manager.redo()
    elif command == "reset":
        return manager.reset_session()
    elif command == "print_all":
        return manager.all__data_string()
    elif command == "print_group":
        return manager.group_data_string()
    opcode, addressing_mode = command.split()
    if opcode == "add":
        return manager.add(addressing_mode[0], addressing_mode[1], addressing_mode[2], decryption_key)
    elif opcode == "get":
        return manager.get(addressing_mode[0], addressing_mode[1], decryption_key)
    elif opcode == "delete":
        return manager.delete(addressing_mode[0], addressing_mode[1])
    else:
        raise manager_exceptions.CommandNotFoundException

