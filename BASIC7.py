import math

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height
hypotenuse = math.sqrt(base**2 + height**2)
perimeter = base + height + hypotenuse

print(f"The area of the triangle is: {area}")
print(f"The perimeter of the triangle is: {perimeter}")
