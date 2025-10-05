def area_of_circle(circles):
    area_circle_list = []
    for num in circles:
        area_circle = 3.14 * (num ** 2)
        area_circle_list.append(area_circle)
    return area_circle_list

def area_of_rectangle(rectangles):
    area_rectangle_list = []
    for length, width in rectangles:
        area_rectangle = length * width
        area_rectangle_list.append(area_rectangle)
    return area_rectangle_list
