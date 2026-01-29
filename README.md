This is the source code of a simple calculator written in Python. I will try to explain the code as simple as possible.



def my_sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def fulldivison(a,b):
    return a//b
def modulus(a,b):
    return a%b

These functions were written to demonstrate the usage of functions. I think they do not need explanation. 

while True:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    op = input("Enter the operation(+, -, *, /, //, % , 'exit'): ")
    if op=="*":
        print(multiply(first_number,second_number))
    elif op=="/":
        if second_number!=0:
            print(divide(first_number,second_number))
        else:
            print("We can not divide by zero!")
    elif op=="//":
        if second_number!=0:
            print(fulldivison(first_number,second_number))
        else:
            print("We can not divide by zero")
    elif op=="+":
        print(my_sum(first_number,second_number))
    elif op=="%":
        print(modulus(first_number,second_number))
    elif op=="-":
        print(subtract(first_number,second_number))
    elif op=="exit":
        break
    else:
        print("You entered a wrong operator")
        continue


Let's look at the loop. The variables named first_number and second_number are used to store the values of the first and second number and their type is float as a calculator should have the ability to 
work with float numbers. The operator variable should be given strings like +,-,/,//,%,*,"exit". After that the if and elif statements are used to call the functions we wrote earlier.

I want to point out that when we are dividing, the second number can not be zero, so in order to prevent an error, we should write an if/else statement inside the elif that tries to match / or //,
we could also write try/except but I preferred if/else statements. If the op variable does not match any of the expected math operators, then the user will be motified that he or she entered a wrong operator and
they will have the ability to choose an operator again which is provided by the continue. That's basically it












