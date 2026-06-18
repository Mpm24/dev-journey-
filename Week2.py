# Week 2 - Grade Tracker
# Goal: practice lists and loops


number_of_grades = int(input("Enter the number of grades: "))

grades = [] 

for i in range(number_of_grades):
    grade = int(input(f"Enter grade {i+1}: "))
    grades.append(grade)

average = sum(grades) / len(grades)

print("")
print(f"Your grades: {grades}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
print(f"Average grade: {average:.2f}")


if average >= 70:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")