	Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
             Unit                                    Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000) 
------------------------------------------------------------------------------------------------------------------------------------------------
unit=int(input("enter no of unit consumption "))
if unit<=100:
    print ("no charge applicable")
elif 100<unit<=200:
    charge=5*unit
    print("the charge for",unit," is ", charge)
elif 200<unit:
    charge=10*unit
    print("the charge for",unit," is ", charge)
