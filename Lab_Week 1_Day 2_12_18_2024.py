#Problem 1:

#Write a program to input 3 sides of a triangle
#and calculate and print its area.

import math
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The entered sides do not form a valid triangle.")
