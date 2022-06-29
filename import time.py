import time

time.sleep(1)
print("Welcome...")
welcome = input("Do you have an acount? y/n")
if welcome == "n":
    username = input("Enter a username:")
    password = input("Enter a password:")
    password1 = input("Confirm password:")
if password != password1:
    print("Passwords do NOT match!")
username = input("Enter a username:")
password = input("Enter a password:")
password1 = input("Confirm password:")
text_file = open(username+ ".txt", "w")
text_file.write(username+":"+password)
text_file.close()
login1 = input("Login:")
login2 = input("Password:")
f = file = open(login1+".txt", "r")
if(file.readline())== (login1+":"+login2):
    print("Welcome")

if welcome == "y":
    login1 = input("Login:")
    login2 = input("Password:")
    f = file = open(login1+".txt", "r")
if(file.readline())== (login1+":"+login2):
    print("Welcome")
if(file.readline())!= (login1,":",login2):
    print("Incorrect username or password.")
time.sleep(1)
login1 = input("Login:")
login2 = input("Password:")
text_file = open(login1+ ".txt", "r")
login1 = input("Login:")
login2 = input("Password:")
f = file = open(login1+".txt", "r")
