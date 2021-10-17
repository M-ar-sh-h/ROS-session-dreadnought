#!/usr/bin/python3

from demo.srv import SquareSumThreeInts, SquareSumThreeIntsResponse
import rospy


def handle_square_sum_three_ints(req):
    print(
        "Returning [%s^2 + %s^2 + %s^2 = %s]"
        % (req.a, req.b, req.c, (req.a ** 2 + req.b ** 2 + req.c ** 2))
    )
    return SquareSumThreeIntsResponse(req.a ** 2 + req.b ** 2 + req.c ** 2)


def square_sum_three_ints_server():
    rospy.init_node("square_sum_three_ints")
    s = rospy.Service(
        "square_sum_three_ints", SquareSumThreeInts, handle_square_sum_three_ints
    )
    print("Ready to squaresum three ints.")
    rospy.spin()


if __name__ == "__main__":
    square_sum_three_ints_server()
