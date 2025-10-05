radius = [4, 6]
def area_of_circle(radius):
    area_circle_list = []
    for num in radius:
        area_circle = 3.14 * (num ** 2)
        area_circle_list.append(area_circle)
    return area_circle_list

area_circle_list = area_of_circle(radius)
