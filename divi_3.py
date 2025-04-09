7. Write a program to take a number from user. Check whether the last digit of that is divisible by 3 or not.
------------------------------------------------------------------------------------
num=int(input("enter number "))
last_digit=num%10
if last_digit%3==0:
    print(num,"is divisible by 3")
else :
    print(num,"not divisible by 3")
