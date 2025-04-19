import sys

if len(sys.argv) != 2:
    print("Usage: python3 circle.py <radius>")
    sys.exit(1)

radius = float(sys.argv[1])

area = 3.14 * (radius**2)
print(f"The area of the circle is: {area}")
perimeter = 2 * 3.14 * radius
print(f"The perimeter of the circle is: {perimeter}")
