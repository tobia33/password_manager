from collections import deque
import copy
import manager_support
import manager_exceptions


"""
structure data_file:
group1-key1:value1,key2:value2;group2-key1:value1
"""


class Manager:
    """
    The Manager class manages the data_file a file containing groups, key and
    values.
    The passwords and usernames are divided in groups, and each group
    has it's keys and values.
    Keys are what we are storing, values the actual value of what we
    are storing
    The abstract structure is:
    {group1 : {key1 : value1, key2 : value2}, group2 : {key1 : value1}}
    a more practical example:
    {Gmail :
    {username : tobia@gmail.com, password : tobia33, pass_code : 1933420},
    GitHub : {...}}
    """

    def __init__(self, data_file):
        """ initialize the manager loading the data from data_file
            that had been previously stored"""
        self.data_file = data_file
        self.data_table = self.load_data()
        self.stack_undo = deque(maxlen=5)
        self.stack_redo = deque(maxlen=5)
        self.backup = copy.deepcopy(self.data_table)

    def load_data(self):
        """ load data from the 'data' file and return
            a nested dictionary that is the data_table """
        data_table = {}
        file = open(self.data_file, encoding="utf-8", mode="r")
        raw_data = file.read()
        file.close()
        if raw_data:
            group_list = raw_data.split(";")
            for group_couple in group_list:
                group, group_values = group_couple.split("-")
                group_values = group_values.split(",")
                for i in range(len(group_values)-1):
                    group_values[i] = group_values[i].split(":")
                # group_values is now a list of lists
                data_table[group] = dict(group_values)
        return data_table

    def write_data(self):
        """ write data from the data_table to the 'data' file """
        data_string = ""
        for group, dictionary in self.data_table.items():
            data_string += group + "-"
            for key, value in dictionary:
                data_string += key + ":" + value + ","
            data_string += ";"
        file = open(self.data_file, encoding="utf-8", mode="w")
        file.write(data_string)
        file.close()

    def add(self, group, key, value, decryption_key):
        """ add a key and a value inside the chosen group
            the  value will be encripted with the given decrrption key
            if decription_key is False the value will not be encripted"""
        # decryption_key is assumed to be the right one or the value False
        # proper checks are done elsewhere
        # salvo contenuto nello stack
        self.stack_undo.append(copy.deepcopy(self.data_table))
        if decryption_key is not False:
            value = manager_support.encript(value, decryption_key)
        self.data_table[group][key] = value

    def get(self, group, key, decryption_key):
        """ get the value for the specified group and key
            the value will be decripted using the given decryption key
            if decryption_key is false the value will not be decripted
            raise an error if the group or the key are not found"""
        if group not in self.data_table:
            raise manager_exceptions.GroupNotFoundException
        if key not in self.data_table[group]:
            raise manager_exceptions.KeyNotFoundException
        value = self.data_table[group][key]
        if decryption_key is not False:
            value = manager_support.decript(value, decryption_key)
        return value

    def delete(self, group, key=None):
        """ deletes the specified key or group
            raise an error if the group or the key are not found"""
        # salvo contenuto nello stack
        self.stack_undo.append(copy.deepcopy(self.data_table))
        if group not in self.data_table:
            raise manager_exceptions.GroupNotFoundException
        if key is not None:
            if key not in self.data_table[group]:
                raise manager_exceptions.KeyNotFoundException
            self.data_table[group].pop(key)
        else:
            self.data_table.pop(group)

    def undo(self):
        """ undo your most recent change to the data_table
        either add or delete """
        self.stack_redo.append(copy.deepcopy(self.data_table))
        self.data_table = self.stack_undo.pop()

    def redo(self):
        """ redo your most recent change to the data_table
        either add or delete """
        self.stack_undo.append(copy.deepcopy(self.data_table))
        self.data_table = self.stack_redo.pop()

    def reset_session(self):
        """ uses the backup to reset the session """
        self.stack_undo.append(copy.deepcopy(self.data_table))
        self.data_table = self.backup

    def all__data_string(self):
        """ prints all the data in data_table """
        data_string = ""
        for group in self.data_table:
            data_string += self.group_data_string(group) + "\n"
        return data_string

    def group_data_string(self, group):
        """ prints the data in data_table of a single group  """
        if group not in self.data_table:
            raise manager_exceptions.GroupNotFoundException
        data_string = "\t# " + group + ":"
        for key in self.data_table[group]:
            data_string += + "\n\t\t- " + key
        return data_string
