#!/usr/bin/python3

import rospy
import math
import time
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rospy.init_node('turtle_mad_angle_make_a_triangle', anonymous=False)
move = Twist()
go_straight = 2*(math.pi)*180/360
# Sum of all angles of a regular star pentagon = 180°
# There are 5 angles. so each angle = 180°/5 = 36°
# Therefore, turtle should rotate by = 180°-36° = 144°
rotate_angle = 2*(math.pi)*144/360

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


def star():

    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)

    while not rospy.is_shutdown():
        for _ in range(5):
            straight()
            rotate()
        break        


if __name__ == '__main__':
    try:
        star()
    except rospy.ROSInterruptException:
        pass