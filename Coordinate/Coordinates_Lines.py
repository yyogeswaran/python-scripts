""" Coordinate Geometry Program
    for basic operations
"""

# Function imports
import math
import sys
import numpy

def distance(x1, y1, x2, y2):
    """ Returns the distance of two points """

    bracket1 = (x1 - x2) ** 2
    
    bracket2 = (y1 - y2) ** 2
    
    bracket3 = numpy.sqrt(bracket1 + bracket2)
    
    return "the distance is %s" % (bracket3)

def midpoint(x1, y1, x2, y2):
    """ Returns the coordinates of the midpoint """

    bracket1 = (x1 + x2)/2
    bracket2 = (y1 + y2)/2

    return "x: %s, y: %s." % (bracket1, bracket2)

def gradient(x1, y1, x2, y2):
    """ Returns the gradient of the line """
    
    bracket3 = (y2-y1) / (x2-x1)

    return bracket3

def main():
    while True:
        print "Choose your operation:"
        print "    1. Find distance"
        print "    2. Find midpoint"
        print "    3. Find gradient"
        print "    4. Exit Program."

        response = raw_input("Choose: ")

        # Response logic
        if int(response) == 1:
            x1 = float(raw_input("x1: "))
            y1 = float(raw_input("y1: "))
            x2 = float(raw_input("x2: "))
            y2 = float(raw_input("y2: "))

            print distance(x1, y1, x2, y2)

        elif int(response) == 2:
            x1 = float(raw_input("x1: "))
            y1 = float(raw_input("y1: "))
            x2 = float(raw_input("x2: "))
            y2 = float(raw_input("y2: "))

            print midpoint(x1, y1, x2, y2)

        elif int(response) == 3:
            x1 = float(raw_input("x1: "))
            y1 = float(raw_input("y1: "))
            x2 = float(raw_input("x2: "))
            y2 = float(raw_input("y2: "))

            print gradient(x1, y1, x2, y2)

        elif int(response) == 4:
            print "Terminating"
            break

        else:
            print "Error - enter an number between 1 - 4"

#function call
main()
