import random

CHARACTER = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst123456789!@#$%^&*_-+~|:?"

A_Password = input("Amout of password do you need : ")
A_Password = int(A_Password)

L_Password = int(input("enter the length of password : "))

p = 1
while A_Password:
    P_string = " "
    x = L_Password
    while x:
        P_string += random.choice(CHARACTER)
        x -= 1
    print(f"your {p} passord is : {P_string}")
    A_Password -= 1
    p += 1