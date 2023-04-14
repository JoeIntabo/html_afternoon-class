# if elif else statement
marks=int(input("Key in your marks:"))
if marks>80 and marks<=100:
    print("You scored an A")
elif marks>60 and marks<=80:
    print("You have a B")
elif marks>40 and marks<=60:
    print("You have a C")
elif marks>30 and marks<=40:
    print("You have a D")
elif marks>=0 and marks<30:
    print("You have an E")
else:
    print("Wrong input")

age=int(input("Key in your age:"))
if age>50 and age<=100:
    print("You are of old age")
elif age>35 and age<=50:
    print("You are headed for old age")
elif age>21 and age<=35:
    print("You are an adult ")
elif age>13 and age<=21:
    print("You are a teenager")
elif age>0 and age <=13:
    print("You are still a child")
else:
    print("Wrong age input")
