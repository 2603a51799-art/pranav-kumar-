m = int(input("Enter the marks of the student: "))

if m >= 91:
    print("Student passed the examination with Excellent grade!!")
elif m >= 81:
    print("Student passed the examination with Very Good grade!!")
elif m >= 71:
    print("Student passed the examination with Good grade!!")
elif m >= 61:
    print("Student passed the examination with Average grade!!")
elif m>= 40:
    print("Student passed the examination with Poor grade!!")
else:
    print("Student failed the examination!!")