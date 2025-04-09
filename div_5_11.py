6. Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message. 
-----------------------------------------------------------------------------------------------------------------------------------
num = int(input("enter number "))
if num%5==0 and num%11==0:
    print(num,"is divided by 5 and 11")
else 
    print(num,"is not divisible by 5 and 11")
