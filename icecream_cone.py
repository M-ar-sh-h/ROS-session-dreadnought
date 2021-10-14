#!/usr/bin/python3

import rospy
import math as m
import time
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rospy.init_node('turtle_in_a_dream_eat_a_icecream', anonymous=False)
move = Twist()
SIDE_LENGTH = 2*(m.pi)*150/360
TOP_LENGTH = 2*(m.pi)*75/360
TOPSIDE_ANGLE = 2*(m.pi)*104.95/360
SIDESIDE_ANGLE = 2*(m.pi)*150/360
ICECREAM_ANGLE = 2*(m.pi)*330/360

time.sleep(2)


def make_side():
    move.linear.x = SIDE_LENGTH
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)


def topside_rotate():
    move.linear.x = 0.0
    move.angular.z = TOPSIDE_ANGLE
    pub.publish(move)
    time.sleep(1)


def make_top():
    move.linear.x = TOP_LENGTH
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)


def sidesiderotate():
    move.linear.x = 0.0
    move.angular.z = SIDESIDE_ANGLE
    pub.publish(move)
    time.sleep(1)


def make_icecream_angle():
    move.linear.x = 0.0
    move.angular.z = ICECREAM_ANGLE
    pub.publish(move)
    time.sleep(1)


def make_icecream():
    for _ in range(2):
        move.linear.x = 2.5
        move.angular.z = 2.5
        pub.publish(move)
        time.sleep(1)
        

def icecream():

    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(1)

    while not rospy.is_shutdown():
        make_side()
        topside_rotate()
        make_top()
        topside_rotate()
        make_side()
        sidesiderotate()
        make_side()
        make_icecream_angle()
        make_icecream()
        break                 


if __name__ == '__main__':
    try:
        icecream()
    except rospy.ROSInterruptException:
        pass
