import random 

content = 5 

isAgine = True
isValid = False

num1 = random.randint(0, 100)
print(num1)
print(content)
num2 = int(input("enter your number...(betwin 0 to 100 )"))

if(num2 > 100 ) : 
    isValid = True

while (isValid) :
    num2 = int(input("enter your number...(betwin 0 to 100 )"))
    if(num2 > 100 ) : 
        isValid = True
    else :
        isValid = False


while(isAgine or content == 5) :
    content -= 1 
    if(num1 == num2):
        print("you win...")
        if(isAgine):
            num3 = int(input("do you want agine game...(1 / 0)"))
            if(num3 == 1) :
                isAgine = True
                num1 = random.randint(0, 100)              
                print(num1)
                content = 5
                print(content)
                num2 = int(input("enter your number..."))
                if(num2 > 100 ) : 
                    isValid = True
                
                while (isValid) :
                    num2 = int(input("enter your number...(betwin 0 to 100 )"))
                    if(num2 > 100 ) : 
                        isValid = True
                    else :
                        isValid = False
            else :
                isAgine = False
                break
    elif(num1 > num2):
        print(content)
        print("the number is lattle")
        num2 = int(input("enter your number..."))
        if(num2 > 100 ) : 
            isValid = True
                
        while (isValid) :
            num2 = int(input("enter your number...(betwin 0 to 100 )"))
            if(num2 > 100 ) : 
                isValid = True
            else :
                isValid = False
        
        
    elif(num1 < num2):
        print(content)
        print("the number is big")
        num2 = int(input("enter your number..."))
        if(num2 > 100 ) : 
            isValid = True
                
        while (isValid) :
            num2 = int(input("enter your number...(betwin 0 to 100 )"))
            if(num2 > 100 ) : 
                isValid = True
            else :
                isValid = False
        
    

    if(0 >= content) :
        isAgine = False
        print("you lose")
        print(num1)
        if(content == 5):
            print("نمونه ای")
        elif(content == 4):
                print("بسیار خوبی ")
        elif(content == 3):
            print("خوب")
        elif(content == 2):
            print("قبول")
        elif(content == 1):
            print("با شانس یردی")



    