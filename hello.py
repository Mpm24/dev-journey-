#Week 1 - Hello World script 
#Goal: practice inpout, variable, and basic math


name = input("What is yuour name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year
years_ahed = 60 - age

print("")
print(f"Welcome, {name}!")
print(f"you are {age} years old")
print(f"You have {years_ahed} years of coding ahed of you.")