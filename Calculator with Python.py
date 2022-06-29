from ast import operator
from random import choice


print("Enter Your Choice")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

choice = input("Enter Your Operator:")

num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))

if choice == "1":
    print(num1, "+", num2, "=", (num1+num2))

elif choice == "2":
    print(num1, "-", num2, "=", (num1-num2))

elif choice == "3":
    print(num1, "*", num2, "=", (num1*num2))

elif choice == "4":
    print(num1, "/", num2, "=", (num1/num2))
else:
    print("Invalid Number")