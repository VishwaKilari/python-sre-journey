# Variables and Data Types
# Author : Vishwa

name = "Vishwa"
age = 25
height = 5.9
is_engineer = True

'''
print(name)
print(age)
print(height)
print(is_engineer)
print(25+10)
print("25"+"10")
print(type(name))
print(type(age))
print(type(height))
print(type(is_engineer))
'''
user_name = input("what is your name?\n")
user_age = int(input("what is your age?\n"))
remaining_years = 60 - (user_age)
#print(f"Hello {user_name}, you are {user_age} years old and you have {remaining_years} years until you are 60")
#print(remaining_years)
print("Hello "+ str(user_name) + ", you are " + str(user_age) + " years old and you have " + str(remaining_years) + " years until you are 60")
