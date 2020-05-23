import turtle
import math

def get_outer_angle(angle):
    """Calculate the outer angle of the given conner

    :angle: inner angle
    :returns: outer angle
    """
    return 180 - angle

def get_angle_btween_sides(adjacent, opposite, hypotenuse):
    """Calculate angles between adjacent and opposite,
    hypotenuse and opposite

    :adjacent: length of the adjacent side
    :opposite: length of the opposite side
    :hypotenuse: length of the hypotenuse
    :returns: tuple(ao-angle, ho-angle)
    """
    ao_angle = None
    ho_angle = None
    ah_angle = None
    
    ao_angle = round(math.degrees(math.acos((math.pow(adjacent, 2) + math.pow(opposite, 2) - math.pow(hypotenuse, 2)) / (2 * adjacent * opposite))), 2)

    ho_angle = round(math.degrees(math.acos((math.pow(opposite, 2) + math.pow(hypotenuse, 2) - math.pow(adjacent, 2)) / (2 * opposite * hypotenuse))), 2)

    return ao_angle, ho_angle


def draw(adjacent, opposite, hypotenuse, ao_angle, ho_angle, start_x=0, start_y=0):
    """Draw the triangle for given measurements

    :adjacent: length of the adjacent side
    :opposite: length of the opposite side
    :hypotenuse: length of the hypotenuse
    :ao_angle: inner angle of the adjacent and opposite
    :ho_angle: inner angle of the hypotenuse and opposite
    :start_x: position to start on the X axis
    :start_y: opposite to start on the Y axis
    """
    # Initialize turtle instance
    t = turtle.Turtle()

    # Set drawing off while moving the pen
    t.penup()

    # Set the start position of the window. Default 0,0
    t.setpos(start_x,start_y)

    # Set drawing on after moving the pen
    t.pendown()

    # Set the heading of the pen to backwards. More options available on the reference docs
    # https://docs.python.org/3/library/turtle.html#turtle.setheading
    t.setheading(180)

    # Set the drawing speed. More options available on the reference docs
    # https://docs.python.org/3/library/turtle.html#turtle.speed
    t.speed(3)

    t.forward(adjacent)

    t.right(get_outer_angle(ao_angle))
    t.forward(opposite)

    t.right(get_outer_angle(ho_angle))
    t.forward(hypotenuse)


def main():
    # create a new window
    w = turtle.Screen()

    # Right angle triangle
    adjacent = 100
    opposite = 100
    hypotenuse = 141.42
    ao_angle, ho_angle = get_angle_btween_sides(adjacent, opposite, hypotenuse)
    draw(adjacent, opposite, hypotenuse, ao_angle, ho_angle, 0, 50)

    # Equilateral triangle
    adjacent = 100
    opposite = 100
    hypotenuse = 100
    ao_angle, ho_angle = get_angle_btween_sides(adjacent, opposite, hypotenuse)
    draw(adjacent, opposite, hypotenuse, ao_angle, ho_angle, 200, 50)

    # Isosceles triangle
    adjacent = 150
    opposite = 167.71
    hypotenuse = 167.71
    ao_angle, ho_angle = get_angle_btween_sides(adjacent, opposite, hypotenuse)
    draw(adjacent, opposite, hypotenuse, ao_angle, ho_angle, 0, -200)

    # Close the drawing window after user clicks on the window
    # https://docs.python.org/3/library/turtle.html#turtle.exitonclick
    w.exitonclick()

# Force the application to run main()
# without this script will end without running anything
if __name__ == '__main__':
    main()
