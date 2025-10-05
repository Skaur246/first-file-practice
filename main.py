from output import area_of_shapes
from area_calculation import area_of_circle

# Calculating area of rectangles
length1 = 10
width1 = 5
area_rectangle1 = length1 * width1

length2 = 15
width2 = 7
area_rectangle2 = length2 * width2

# Calculating area of circles
radius = [4, 6]
area_circle_list = area_of_circle(radius)

# printing result
area_of_shapes(area_rectangle1, area_rectangle2, area_circle_list[0], area_circle_list[1])