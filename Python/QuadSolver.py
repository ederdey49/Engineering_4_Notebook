from math import sqrt #import the square root function

print("Quadratic Solver. Enter the coefficients for ax^2 + bx + c = 0")
a = input("Enter a:") #the user gives the coefficients (read in as strings)
b = input("Enter b:")
c = input("Enter c:")

def quadFunction(coef1, coef2, coef3): #create a method with the coefficients as arguments that returns an array of the roots
    x = int(coef1) #create internal variables by casting string arguments as ints
    y = int(coef2)
    z = int(coef3)

    disc = (y*y - 4*x*z) #find the discriminant (b^2-4ac)

    if(disc < 0): #if the discriminant is less than 0 (meaning the roots are imaginary)
        return; #return nothing (as there are no real solutions)
    else:
        sol1 = (-y + sqrt(disc))/(2*x) #the first solution is -b + the square root of the discriminant
        sol2 = (-y - sqrt(disc))/(2*x) #the second solution is -b - the square root of the discriminant
        if(sol1 != sol2): #if these aren't the same number (meaning the function has two roots, not one)
            array = [sol1, sol2] #set the solution array to both solutions
        else: #if they are the same (only one solution)
            array = [sol1] #set the solution array to just the one solution
        
        return array; #return the solution array

print("Roots are " + str(quadFunction(a, b, c))) #display the solutions of quadFunction with the user-generated coefficients

            
