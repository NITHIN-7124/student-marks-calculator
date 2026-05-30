print("welcome to student marks calculator")
name1 = input(" enter student name1:")
marks1 = int(input("enter the   student marks1:"))
name2 = input("enter the student   name2:")
marks2 = int(input("enter the  student marks2:"))

print("student name :", name1 )
print(" student marks:",marks1 )
print("student name :", name2 )
print(" student marks:",marks2 )



if marks1 >= 85:
    print(name1, "EXCELLENT A GRADE")

elif marks1 >= 35:
    print(name1, "PASS")

else:
    print(name1, "FAIL")
   

if marks2 >= 60:
    print(name2, "excellent")

elif marks2 <= 50:
    print(name2, "PASS")

else :print(name2, "FAIL") 

average(marks1 + marks2)/2
print("average marks:",average)
highest max(marks1 , marks2)
print("highest marks:", highest)



