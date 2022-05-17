import modules.square as square, modules.triangle as triangle


def area(shape_type, side_length):
    if shape_type == "square":
        return square.square_area(side_length)
    elif shape_type == "triangle":
        return triangle.triangle_area(side_length)


def perimeter(shape_type, side_length):
    if shape_type == "square":
        return square.square_perimeter(side_length)
    elif shape_type == "triangle":
        return triangle.triangle_perimeter(side_length)
