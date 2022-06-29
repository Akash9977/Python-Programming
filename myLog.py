from os import name
from turtle import position

def myLog():
    userName=[]
    passwords=[]

    for i in range (1):
        name=input("Register in Name\n").capitalize()
        userName.append(name)
        userName.sort()
        passcode=int(input("Enter Your Password\n"))
        passcode=int(input("confirm  Password\n"))
        passwords.append(passcode)
        passwords.sort()

        name=input("Plz Enter Your User Name\n")
        if name in userName:
            position=userName.index(name)
            passcode=int(input("Plz Enter Your Password\n"))
            if passcode == passwords[position]:
                print("Welcome",name)
            else:
                print("Password in Incorret")

        else:
            print("User Name is Incorret")

myLog()       
