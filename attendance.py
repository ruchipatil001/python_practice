'''1.	A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
Is student is allowed to sit in exam or not.'''
---------------------------------------------------------------------------
total_no_class=int(input("enter total no of class "))
attended_class=int(input("no of class attended "))
percent=(attended_class/total_no_class)*100
if percent<75:
    print(percent,":not allowed to seat in exam")
else :
    print(percent,":allowed to seat in exam")
