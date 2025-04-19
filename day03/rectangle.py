import sys

if len(sys.argv) != 3:
    print("Usage: python3 rectangle.py <height> <width>")
    sys.exit(1)

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
print(f"The area of the rectangle is {area}")

perimeter = (2 * width) + (2 * height)
print(f"The perimeter of the rectangle is {perimeter}")