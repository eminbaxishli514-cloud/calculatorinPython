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