#Alexis Gore
#9/30/25
#P2LAB1
#Measurement of a Circle

radius = float(input("What is the radius of the circle? "))
print("\n")
diameter = 2 * radius
import math
PI = math.pi
circumference = 2 * PI * radius
area = PI * radius**2
print("The diameter of the circle is", f"{diameter:.1f}")
print("\n")
print("The circumference of the circle is", f"{circumference:.2f}")
print("\n")
print("The area of the circle is", f"{area:.3f}")