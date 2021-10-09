#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rospy.init_node('turtle_turtle_go_in_a_circle', anonymous=False)
rate = rospy.Rate(1)
move = Twist()


def circle():

    while not rospy.is_shutdown():
        move.linear.x = 5.0
        move.angular.z = 2.0
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass            
