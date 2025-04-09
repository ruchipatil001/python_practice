A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
Is student is allowed to sit in exam or not. Modify the above question Q1. 
if student has ttendance less than 75% then ask user if he/she has medical cause or not ( 'Y' or 'N' ).  
print "Allow" if he/she has medical cause else not allowed. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------

total_no_class=int(input("enter total no of class "))
attended_class=int(input("no of class attended "))
percent=(attended_class/total_no_class)*100
if percent<75:
    eligible_medical=input("is there any medical cause:Y/N ")
    if(eligible_medical=='Y'):
        print("allow to exam")
    else:
        print("not allowed")
    
else :
    print(percent,":allowed to seat in exam")
