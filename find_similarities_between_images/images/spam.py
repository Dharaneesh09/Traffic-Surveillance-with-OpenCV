#2nd quention
'''
for i in range(1,8):
    if i%2 == 0:
        char = '@'
    else:
        char = "%"
    print(char*i)

    '''
'''
#3rd question
num = int(input("Enter the number : "))
prime = True
for i in range(2,num):
 if num % i == 0:
    prime = False
    break
if prime:
    print("Number is prime")
else:
    print("Number is not prime")
'''

'''
# 4th question

def printnum(summ):
    for i in range(summ):
        if (i%2==0) and (i%3==0):
            print(i)
    return

def sum1(num1 , num2):
    summ = num1 + num2
    printnum(summ)
    return summ
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

sum1(num1,num2)
'''

#5th question

def printLarge(int1, flt1,flt2, flt3):
    a = int1 if int1 > flt1 else flt1
    b = flt2 if flt2 > flt3 else flt3
    res = a if a < b else b
    print(res)
    return

num1 = int(input("Enter the integer : "))
num2 = float(input("Enter 1st float : "))
num3 = float(input("Enter 1st float : "))
num4 = float(input("Enter 1st float : "))
printLarge(num1,num2,num3,num4)