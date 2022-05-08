a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print("****CHOSE YOUR OPERATION*****")
print ('''1. addition
        2.subtition
        3. multipulitiion
        4. divisoun
        5. intteger diviosn
        6. module''')
x = int(input("Enter your operation number:"))


if(x==1):
    print("Your answer is :" , a+b)
if(x==2):
    print("your answer is:", a-b)
if(x==3):
    print("Your answer is :", a*b)
elif(x==4):
    print("Your answer is :", a/b)
elif(x==5):
    print("Your answer is :", a//b)
elif(x==6):
    print("your answer is :", a%b)
else:
    print("You chose wrong operation, Plese select write operation.")

