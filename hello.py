#Week 1 - Hello World script 
#Goal: practice input, variable, and basic math


name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year
years_ahead = 60 - age

print("")
print(f"Welcome, {name}!")
print(f"You are {age} years old")
print(f"You have {years_ahead} years of coding ahead of you.")

if birth_year >= 1946 and birth_year <= 1964:
    print("")
    print("You are a Baby Boomer!")
elif birth_year >= 1965 and birth_year <= 1980:
    print("")
    print("You are a Gen X!")
elif birth_year >= 1981 and birth_year <= 1996:
    print("")
    print("You are a Millenial!")
elif birth_year >= 1997 and birth_year <= 2012: 
    print("")
    print("You are a Gen Z!")
else:
    print("")
    print("You are too old or too young for our list!")