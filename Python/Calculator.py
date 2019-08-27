
a = input("Enter first number: ")
b = input("Enter second number: ")

def doMath( num1, num2, op):
    if(op == 1):
        out = str(float(num1) + float(num2))
    if(op == 2):
        out = str(float(num1) - float(num2))
    if(op == 3):
        out = str(float(num1) * float(num2))
    if(op == 4):
        out = str(round(float(num1) / float(num2), 2))
    if(op == 5):
        out = str(float(num1) % float(num2))
    return out;

print("Addition: " + doMath(a, b, 1))
print("Subtraction: " + doMath(a, b, 2))
print("Multiplication: " + doMath(a, b, 3))
print("Division: " + doMath(a, b, 4))
print("Modulo: " + doMath(a, b, 5))

