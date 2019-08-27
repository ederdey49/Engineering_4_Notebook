from math import sqrt

print("Quadratic Solver. Enter the coefficients for ax^2 + bx + c = 0")
a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")

def quadFunction(coef1, coef2, coef3):
    x = int(coef1)
    y = int(coef2)
    z = int(coef3)

    disc = (y*y - 4*x*z)

    if(disc < 0):
        return;
    else:
        sol1 = (-y + sqrt(disc))/(2*x)
        sol2 = (-y - sqrt(disc))/(2*x)
        if(sol1 != sol2):
            array = [sol1, sol2]
        else:
            array = [sol1]
        
        return array;

print("Roots are " + str(quadFunction(a, b, c)))

            
