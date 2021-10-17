#!/usr/bin/python3

import sys
import rospy
from demo.srv import *


def square_sum_three_ints_client(x, y, z):
    rospy.wait_for_service("square_sum_three_ints")
    try:
        square_sum_three_ints = rospy.ServiceProxy(
            "square_sum_three_ints", SquareSumThreeInts
        )
        response = square_sum_three_ints(x, y, z)
        return response.squaresum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [x y z]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s^2 + %s^2 + %s^2" % (x, y, z))
    print("%s^2 + %s^2 + %s^2 = %s" % (x, y, z, square_sum_three_ints_client(x, y, z)))
