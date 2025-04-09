It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 400 then it is leap year  
•	otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year.
-------------------------------------------------------------------------------------------------------------
year=int(input("enter year "))
if year%100==0 and year%400:
    print(year,"is leap year")
elif year%4==0 and year%100!=0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
 
