#!/usr/bin/python3

import rospy
import math
import time
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rospy.init_node('turtle_mad_angle_make_a_triangle', anonymous=False)
move = Twist()
n = int(input("Number of sides: "))
go_straight = 2*(math.pi)*90/360
rotate_angle = 2*(math.pi)*(360/n)/360

time.sleep(2)


def straight():
    move.linear.x = go_straight
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)


def rotate():
    move.linear.x = 0.0
    move.angular.z = rotate_angle
    pub.publish(move)
    time.sleep(1)


def polygon():
    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)

    while not rospy.is_shutdown():
        if n>1:
            for _ in range(n):
                straight()
                rotate()
        else:
            rotate()  
        break    


if __name__ == '__main__':
    try:
        polygon()
    except rospy.ROSInterruptException:
        pass
