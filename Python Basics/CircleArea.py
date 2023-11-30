# Write a Python program that calculates the area of a circle based on the radius entered by the user.

from math import pi

r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2

# Display the result, including the radius and calculated area
print("The area of the circle with radius " + str(r) + " is: " + str(area))
