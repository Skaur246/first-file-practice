from output import area_of_shapes
from area_calculation import area_of_circle
from area_calculation import area_of_rectangle

# Calculating area of rectangles
rectangle_parameter = [(10, 5), (15, 7)]
area_rectangle_list = area_of_rectangle(rectangle_parameter)

# Calculating area of circles
radius = [4, 6]
area_circle_list = area_of_circle(radius)

# printing result
area_of_shapes(area_rectangle_list[0], area_rectangle_list[1], area_circle_list[0], area_circle_list[1])