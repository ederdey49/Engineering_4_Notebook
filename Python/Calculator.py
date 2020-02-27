
a = input("Enter first number: ") #asks for the user to input a number and saves it as 'a'
b = input("Enter second number: ") #same for b

def doMath( num1, num2, op): #function that actually does the math, takes the 2 variables and a number telling it what operation to do
    if(op == 1): 
        out = str(float(num1) + float(num2)) #return the sum of the variables
    if(op == 2):
        out = str(float(num1) - float(num2)) #return the difference of the variables
    if(op == 3):
        out = str(float(num1) * float(num2)) #return the product of the variables
    if(op == 4):
        out = str(round(float(num1) / float(num2), 2)) #return the quotient of the variables
    if(op == 5):
        out = str(float(num1) % float(num2)) #return the modulo of the variables
    return out;

print("Addition: " + doMath(a, b, 1)) #prints all of the operations
print("Subtraction: " + doMath(a, b, 2))
print("Multiplication: " + doMath(a, b, 3))
print("Division: " + doMath(a, b, 4))
print("Modulo: " + doMath(a, b, 5))

