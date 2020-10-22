import json
import sys
# getting user input
# userInput = input("Enter a name:")
# print("userInput = " + userInput)

# read the birthday json file (the path to your file may be different than mine)
# use the full path if that helps, for example
# pathToFile = 'E:/Users/gabriel/GitHub/evc-cit134a-python-data-structures/src/birthday.json'

# you can use a shorter relative path too
pathToFile = 'E:/Desktop/python/birthday.json' 

with open(pathToFile, 'r') as openfile: 
  
    # Reading from json file 
    birthdayJSON = json.load(openfile) 

birthdayDictionary = {}

# loop json list of data and put each name into a dictionary 
for record in birthdayJSON:

    # fetch name and birthday   
    name = record["name"]   
    birthday = record["birthday"]    
    birthdayDictionary[name] = birthday

repeat_flag = ""
while repeat_flag != "q": # While loop
    flagval = False
    # Search field
    print("Please choose from the following selection")
    print("1) First name")
    print("2) Last name")
    selection = input("Please enter 1 or 2: ")
    if selection == "1":
        search = input("Please enter the first name: ")
        for name,birthday in birthdayDictionary.items():
            first, last = name.split(" ", 2) #delimiter
            if search.lower() == first.lower():
                flagval = True
                print("Name: %s" % (name))
                print("Birthday: %s" % (birthday))
    elif selection == "2":
        search = input("Please enter the last name: ")
        for name,birthday in birthdayDictionary.items():
            first, last = name.split(" ", 2) #delimiter
            if search.lower() == last.lower():
                flagval = True
                print("Name: %s" % (name))
                print("Birthday: %s" % (birthday))
    else:
        sys.exit("Incorrect entry")

    if flagval == False:
        print("%s was not found" % (search))
    repeat_flag = input("Would you like to enter another name?(Type q to quit): ")