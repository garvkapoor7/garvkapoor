#using  functions to make a calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("choose")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
    choose=input("choose=")
    
    if choose in ('1', '2', '3', '4',"add","subtract","multiply","divide"):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choose == '1'or'add':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choose == '2' or 'substract':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choose == '3'or 'multiply':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choose == '4' or 'divide':
            print(n1, "/", n2, "=", divide(n1, n2))
        else:
            print("Error")