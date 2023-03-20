from math import sqrt

# User enters a, b, c
a = float(input('Enter "a": '))
b = float(input('Enter "b": '))
c = float(input('Enter "c": '))

# We use "try except" to avoid terminating the program with a ValueError, caused by finding the root of a negative discriminant.
try:
    sqrtdiscrim = sqrt(b**2 - 4*a*c)

    if sqrtdiscrim > 0:
        x1 = (-b - sqrtdiscrim)/2*a
        x2 = (-b + sqrtdiscrim)/2*a
        print(f"Since the discriminant is greater than zero, the equation has 2 roots: {x1} and {x2}")
    elif sqrtdiscrim == 0:
        x1 = -b/2*a
        print(f"Since the discriminant is zero, the equation has 1 root: {x1}")
except ValueError:
    print("Since the discriminant is less than zero, the equation has no roots")



