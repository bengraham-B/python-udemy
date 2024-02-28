programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of dosing something over and over again.",
}

print(programming_dictionary["loop"])
try:
    print(programming_dictionary["lop"])
except KeyError:
    print("Error regarding the Key")
    
    
#^ Adding a new entry
programming_dictionary["condition"] = "Checks a condition"

print(programming_dictionary) 

#& Creating an empty dictionary 
empty_dict = {}

#! Wipe an existing Dict
# programming_dictionary = {}
# print("After Wipe")
# print(programming_dictionary)

#? Edit an item in a dict
programming_dictionary["Bug"] = "This is a redifined value of bug"

#~ Loop through a dict
for key in programming_dictionary:
    print(key + " - " + programming_dictionary[key])




print(programming_dictionary)
