# Challenge 032

""" Ask for the radius and the depth of a cylinder and work out the total volume (circle area * depth)
rounded to three decimal places. """

from math import pi

radius = float(input('Enter the radius:\n>> '))

depth = float(input('Enter the depth:\n>> '))

cilinder_volume = (pi * radius ** 2 * depth)

print(round(cilinder_volume, 3))

# Other way to display three decimal places

print(f'{cilinder_volume:.2f}')

