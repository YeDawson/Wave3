#Exercise 81:Compute the Hypotenuse
import math
a = float(input("Please insert length of a leg of right triangle: "))
b = float(input("Please insert length of other leg:"))

def ComputeHypotenuse(a, b):
    print("The Hypotenuse of the triangle is: " + str(math.sqrt(a ** 2 + b ** 2)))
ComputeHypotenuse(a, b)