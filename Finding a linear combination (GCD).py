# finding a linear combination of two numbers equal to those two numbers' Greatest Common Denominator:



a = input("What is your first value : ")
b = input("What is your second value : ")


#############################################################################

def gcd(a,b):
 
    # if a and b are both zero, print an error and return 0
    if int(a) == 0 and int(b) == 0:
        print("WARNING: gcd called with both arguments equal to zero.")
        return 0
 
    # make sure a and b are both nonnegative
    if int(a) < 0:
        a = -int(a)
        
    if int(b) < 0:
        b = -int(b)
 
    # if a is zero, the answer is b
    if int(a) == 0:
        return int(b)
    
    # if none of the above:
    d = 1
    t = 1
    while t <= int(a):
        if int(a) % t == 0 and int(b) % t == 0:
            d = t
        t += 1
 
    return d
############################################################################

print(str(gcd(a,b)))



#############################################################################33
# finding the coefficients for the linear Combination:
def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)                  # when assigning variables on the same line the assignment looks like this: a,b,c = (A,B,C).... a --> A , b --> B , c --> C
        return (g, y - (b // a) * x, x)
############################################################################# 
print(egcd(18,24))
 