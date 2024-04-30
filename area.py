import math

def circle(radius):
    '''
    To find the area of the circle 
    circle(radius)
    radius-enter the radius of the circle
    '''
    area=math.pi*radius**2
    return area

def rectangle(length,breath):
    '''
    To find the area of the rectangle
    rectangle(length,breath)
    length-enter the length of rectangle
    breath-enter the breath of the rectangle
    '''

    area=length*breath
    return area

def square(length):
    '''
    To find the area of the circle
    square(length)
    length-enter the length of the square
    '''

    area=length*length
    return area

def triangle(base,height):
    '''
    To find the area of the triangle
    triangle(base,height)
    base-enter the base of the triangle
    height-enter the height of the triangle
    '''

    area=1/2*base*height
    return area