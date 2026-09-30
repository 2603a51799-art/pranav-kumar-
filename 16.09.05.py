name = input("Enter the student name: ")
roll = int(input("Enter the student roll: "))
marks = int(input("Enter the marks: "))
attendance = int(input("Enter the attendance of the student: "))


print(name)
print(roll)


if marks >= 91:
    print("Student got A Grade!!")
elif marks >= 81:
    print("Student got B Grade!!")
elif marks >= 71:
    print("Student got C Grade!!")
else:
    print("Student got D Grade!!")

if attendance >= 75:
    print(f"Student have {attendance}% attendance and eligible for exam!!")
else:
    print(f"Student have only {attendance}% attendance and is not eligible for exam!!")