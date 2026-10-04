#write a python code to accept two number and perform addition substraction multiplicatin division  modulus floor division and exponentiation.

a= float(input("entre the first number:"))
b= float(input("entre the second number:"))

print("addition =",a+b)
print("subtraction=",a-b)
print("multiplication=",a*b)

if b !=0:
    print("division=",a/b)
    print("modulus=",a%b)
    print("floor division =",a//b)
else:

    print("division,modulous and floor division are not pissible with zero.")

print("exponentiation=",a**b)
