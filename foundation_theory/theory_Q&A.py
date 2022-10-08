# # Python methods/functions questions
#
# HOW TO USE THIS FILE
# LINE 1 = function_name() --tab tab tab-- function description
# LINE 2++ = code to run - uncomment to run & check the result
# LINE "Result: (something)" << the result I got running this code on my PC
#
#
# # Python String methods/functions questions
#
#
# # capitalize()	    Returns a string with its first character capitalized and the rest lowercase
# txt = "banana"
# print(txt.capitalize())
# # Result: Banana
#
# # casefold()	        Returns a string with all characters lowercase
# txt = "BaNaNa"
# print(txt.casefold())
# # Result: banana
#
# # center()	        Centers string at specified length, and adds specified character as padding (default character == space)
# txt = "banana"
# print(txt.center(14, "-"))
# # Result: ----banana----
#
# # count()	            Returns the number of times the specified value appears in the string
# txt = "Banana in bananas with banana"
# print(txt.count("banana"))
# # Result: 2
#
# # endswith()	        Returns true if the string ends with the specified value
# txt = "banana?"
# print(txt.endswith("?"))
# # Result: True
#
# # find()	            Searches the string for a specified value and returns the first position of where it was found. If value wasn’t found returns -1
# txt = "banana"
# print(txt.find("n"))
# # Result: 2
#
# # format()	        Formats specified values in a string
# txt = "I got {amt} bananas"
# print(txt.format(amt=5))
# # Result: "I got 5 bananas"
#
# # index()	            Searches the string for a specified value and returns the position of where it was found. If value wasn’t found,  method raises an exception
# txt = "banana"
# print(txt.find("a"))
# # Result: 1
#
# # isalnum()	        Returns True if all characters in the string are alphanumeric
# txt = "banana20"
# print(txt.isalnum())
# # Result: True
#
# # isalpha()	        Returns True if all characters in the string are in the alphabet
# txt = "banana20"
# print(txt.isalpha())
# # Result: False
#
# # isdigit()	        Returns True if all characters in the string are digits
# txt = "520"
# print(txt.isdigit())
# # Result: True
#
# # islower()	        Returns True if all characters in the string are lower case
# txt = "banana"
# print(txt.islower())
# # Result: True
#
# # isnumeric()	        Returns True if all characters in the string are numeric
# txt = "520"
# print(txt.isnumeric())
# # Result: True
#
# # isspace()	        Returns True if all characters in the string are whitespaces
# txt = "          "
# print(txt.isspace())
# # Result: True
#
# # istitle()	        Returns True if the string follows the rules of a title
# txt = "I Got 5 Bananas"
# print(txt.istitle())
# # Result: True
#
# # isupper()	        Returns True if all characters in the string are upper case
# txt = "BANANA"
# print(txt.isupper())
# # Result: True
#
# # join()	            Converts the elements of an iterable into a string
# txt = "I", "got", "5", "bananas"
# print(" ".join(txt))
# # Result: I got 5 bananas
#
# # lower()	            Converts a string into lower case
# txt = "BANANA"
# print(txt.lower())
# # Result: banana
#
# # lstrip()	        Returns a left trim version of the string
# txt = "     banana     "
# print(txt.lstrip())
# # Result: "banana     "
#
# # replace()	        Returns a string where a specified value is replaced with a specified value
# txt = "I got 5 bananas"
# print(txt.replace("bananas", "coconuts"))
# # Result: I got 5 coconuts
#
# # rsplit()	        Splits the string at the specified separator, starting from the right, and returns a list. If no “maxsplit” parameter is specified, the # Result will be the same as “split()”
# txt = "banana, coconut, pineapple"
# print(txt.rsplit(", ", 1))
# # Result: ['banana, coconut', 'pineapple']
#
# # rstrip()	        Returns a right trim version of the string
# txt = "     banana     "
# print(txt.rstrip())
# # Result: "     banana"
#
# # split()	            Splits the string at the specified separator, starting from the left, and returns a list.
# txt = "banana, coconut, pineapple"
# print(txt.split(", ", 1))
# # Result: ['banana', 'coconut, pineapple']
#
# # splitlines()	    Splits the string at the line break and returns a list
# txt = "I got 5 bananas\nHe got 2 bananas"
# print(txt.splitlines())
# # Result: ["I got 5 coconuts", "He got 2 bananas"]
#
# # startswith()	    Returns true if the string starts with the specified value
# txt = "Bananas? I got 5"
# print(txt.startswith("Bananas"))
# # Result: True
#
# # strip()	            Remove spaces at the beginning and at the end of the string and returns a trimmed string
# txt = "   Bananas   "
# print(txt.strip())
# # Result: "Bananas"
#
# # swapcase()	        Swaps cases, lower case becomes upper case and vice versa
# txt = "BaNaNaS"
# print(txt.swapcase())
# # Result: "bAnAnAs"
#
# # title()	            Converts the first character of each word to upper case
# txt = "I got 5 bananas"
# print(txt.title())
# # Result: "I Got 5 Bananas"
#
# # upper()	            Converts a string into upper case
# txt = "banana"
# print(txt.upper())
# # Result: BANANA
#
#
#
# # Python List methods/functions questions
#
#
# # append()	        Adds an element at the end of the list
# list = ["banana", "coconut"]
# list.append("pineapple")
# print(list)
# # Result: ['banana', 'coconut', 'pineapple']
#
# # clear()	            Removes all the elements from the list
# list = ["banana", "coconut"]
# list.clear()
# print(list)
# # Result: list == []
#
# # copy()	            Returns a copy of the list
# list = ["banana", "coconut"]
# list2 = list.copy()
# print(list2)
# # Result: list2 == ['banana', 'coconut']
#
# # count()	            Returns the number of elements with the specified value
# list = ["banana", "coconut", "banana"]
# print(list.count("banana"))
# # Result: 2
#
# # extend()	        Add the elements of a list (or any iterable), to the end of the current list
# list = ["banana", "coconut"]
# list2 = ["pineapple", "mango"]
# list.extend(list2)
# print(list)
# # Result: list == ['banana', 'coconut', 'pineapple', 'mango']
#
# # index()	            Returns the index of the first element with the specified value
# list = ["banana", "coconut"]
# print(list.index("coconut"))
# # Result: 1
#
# # insert()	        Adds an element at the specified position
# list = ["banana", "coconut"]
# list.insert(1, "mango")
# print(list)
# # Result: ['banana', 'mango', 'coconut']
#
# # pop()	            Removes the element at the specified position from the list, and returns removed item
# list = ["banana", "coconut"]
# print(list.pop(1))
# # Result: "coconut"
#
# # remove()	        Removes the first item with the specified value
# list = ["banana", "coconut"]
# list.remove("coconut")
# print(list)
# # Result: list == ['banana']
#
# # reverse()	        Reverses the order of the list
# list = ["banana", "coconut", "pineapple", "mango"]
# list.reverse()
# print(list)
# # Result list == ['mango', 'pineapple', 'coconut', 'banana']
#
# # sort()	            Sorts the list
# list = ["pineapple", "banana", "mango", "coconut"]
# list.sort()
# print(list)
# # Result: list == ['banana', 'coconut', 'mango', 'pineapple']
#
#
#
# # Python Tuple methods/functions questions
#
#
# # count()	            Returns the number of times a specified value occurs in a tuple
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# print(thistuple.count(5))
# # Result: 2
#
# # index()	            Searches the tuple for a specified value and returns the first position of where it was found
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# print(thistuple.index(8))
# # Result: 3
#
#
#
# # Python Dictionary methods/functions questions
#
# # clear()	            Removes all the elements from the dictionary
# pet = {"type": "cat", "name": "Fluff"}
# pet.clear()
# print(pet)
# # Result: pet == {}
#
# # copy()	            Returns a copy of the dictionary
# pet = {"type": "cat", "name": "Fluff"}
# pet2 = pet.copy()
# print(pet2)
# # Result: pet2 == {'type': 'cat', 'name': 'Fluff'}
#
# # fromkeys()	        Returns a dictionary with the specified keys and optional value (default is None)
# keys = ("type", "name")
# print(dict.fromkeys(keys, "X"))
# # Result: {'type': 'X', 'name': 'X'}
#
# # get()	            Returns the value of the specified key
# pet = {"type": "cat", "name": "Fluff"}
# print(pet.get("name"))
# # Result: "Fluff"
#
# # items()	            Returns a list containing a tuple for each key value pair
# pet = {"type": "cat", "name": "Fluff"}
# print(pet.items())
# # Result: dict_items([('type', 'cat'), ('name', 'Fluff')])
#
# # keys()	            Returns a list containing the dictionary's keys
# pet = {"type": "cat", "name": "Fluff"}
# print(pet.keys())
# # Result: dict_keys(['type', 'name'])
#
# # pop()	            Removes the element with the specified key and returns this item
# pet = {"type": "cat", "name": "Fluff"}
# print(pet.pop("type"))
# # Result: "cat"
#
# # popitem()	        Removes the last inserted key-value pair and returns it
# pet = {"type": "cat", "name": "Fluff"}
# print(pet.popitem())
# # Result: ('name', 'Fluff') + the dictionary is only {"type": "cat"}
#
# # setdefault()	    Returns the value of the specified key. If the key does not exist: inserts the key with the specified value.
# pet = {"type": "cat", "name": "Fluff"}
# pet.setdefault("color", "white")
# print(pet)
# # Result: {'type': 'cat', 'name': 'Fluff', 'color': 'white'}
#
# # update()	        Updates the dictionary with the specified key-value pairs
# pet = {"type": "cat", "name": "Fluff"}
# pet.update({"color": "white"})
# print(pet)
# # Result: {'type': 'cat', 'name': 'Fluff', 'color': 'white'}
#
# # values()	        Returns a list of all the values in the dictionary
# pet = {"type": "cat", "name": "Fluff", "color": "white"}
# print(pet.values())
# # Result: dict_values(['cat', 'Fluff', 'white'])
#
#
#
# # Python Set methods/functions questions
#
#
# # add()	            Adds an element to the set
# set = {"banana", "coconut"}
# set.add("pineapple")
# print(set)
# # Result: {'pineapple', 'coconut', 'banana'}
#
# # clear()	            Removes all the elements from the set
# set = {"banana", "coconut"}
# set.clear()
# print(set)
# # Result: set()
#
# # copy()	            Returns a copy of the set
# set = {"banana", "coconut"}
# set2 = set.copy()
# print(set2)
# # Result: {'coconut', 'banana'}
#
# # difference()	    Returns a set containing the difference between two or more sets
# set = {"banana", "coconut", "mango"}
# set2 = {"coconut", "pineapple"}
# print(set.difference(set2))
# # Result: {'mango', 'banana'}
#
# # intersection()	    Returns a set containing matching elements of two or more sets
# set = {"banana", "coconut", "mango"}
# set2 = {"coconut", "pineapple"}
# print(set.intersection(set2))
# # Result: {'coconut'}
#
# # issubset()	        Returns a boolean (T/F) whether another set contains this set or not
# set = {"coconut", "pineapple"}
# set2 = {"banana", "coconut", "mango", "pineapple"}
# print(set.issubset(set2))
# # Result: True
#
# # issuperset()	    Returns a boolean (T/F) whether this set contains another set or not
# set = {"banana", "coconut", "mango", "pineapple"}
# set2 = {"banana", "coconut"}
# print(set.issuperset(set2))
# # Result: True
#
# # pop()	            Removes a random element from the set and returns it
# set = {"banana", "coconut", "mango"}
# print(set.pop())
# # Result: each time different 1 random item of the 3 elements in my set
#
# # remove()	        Removes the specified element from the set
# set = {"banana", "coconut", "mango"}
# set.remove("banana")
# print(set)
# # Result: {'coconut', 'mango'}
#
# # symmetric_difference()	Returns a set with the differences of two sets, so a set containing all items from both sets except the duplicates
# set = {"banana", "coconut", "mango"}
# set2 = {"coconut", "pineapple"}
# print(set.symmetric_difference(set2))
# # Result: {'pineapple', 'banana', 'mango'}
#
# # union()	            Returns a set containing all unique items from both sets (duplicates will only appear once)
# set = {"banana", "coconut", "mango"}
# set2 = {"coconut", "pineapple"}
# print(set.union(set2))
# # Result: {'banana', 'mango', 'coconut', 'pineapple'}
#
# # update()	        Updates a set with values from a set or an iterable
# set = {"banana", "coconut", "mango"}
# set2 = {"coconut", "pineapple"}
# set.update(set2)
# print(set)
# # Result: {'banana', 'mango', 'pineapple', 'coconut'}
#
#
#
# # Python File methods/functions questions
#
#
# # read()	            Returns the specified number of bytes from the file - if no argument provided, reads the whole file.
# with open("banana.txt", "r") as f:
#     print(f.read())
# # Result: the whole content of banana.txt file
#
# # readline()	        Returns the first line from the file
# with open("banana.txt", "r") as f:
#     print(f.readline())
# # Result: the first line of banana.txt file
#
# # readlines()	        Returns a list containing each line in the file as a list item
# with open("banana.txt", "r") as f:
#     print(f.readlines())
# # Result: a list of lines of banana.txt file
#
# # write()	            Writes the specified string to the file. Where the text will be inserted depends on the file mode and stream position.
# # "a" : appends - the text will be inserted at the end of the file
# # "w" : the file will be emptied before the text insertion - overwrites
# with open("banana.txt", "a") as f:
#     f.write("Bananas were here!")
# # Result: "Bananas were here!" was added at the end of the banana.txt file
#
# # writelines()	    Writes a list of strings to the file. Text location is decided the same way as with the write() method.
# with open("banana.txt", "a") as f:
#     f.writelines(["Bananas were here!", "And they will come back!"])
# # Result: Two lines as will be added at the end of the banana.txt file
