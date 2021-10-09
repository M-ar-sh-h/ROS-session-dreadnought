#!/usr/bin/python3

import rospy
import math
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def square():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    rospy.init_node('turtle_rare_go_in_a_square', anonymous=False)
    rate = rospy.Rate(1)
    move = Twist()
    go_straight = 2*(math.pi)*90/360
    right_angle = 2*(math.pi)*90/360

    while not rospy.is_shutdown():
        move.linear.x = 0.0
        move.angular.z = 0.0
        pub.publish(move)
        rate.sleep()
        
        for _ in range(4):
            move.linear.x = go_straight
            move.linear.y = 0.0
            move.linear.z = 0.0
            move.angular.x = 0.0
            move.angular.y = 0.0
            move.angular.z = 0.0
            pub.publish(move)
            rate.sleep()

            move.linear.x = 0.0
            move.linear.y = 0.0
            move.linear.z = 0.0
            move.angular.x = 0.0
            move.angular.y = 0.0
            move.angular.z = right_angle
            pub.publish(move)
            rate.sleep()

        break    


if __name__ == '__main__':
    try:
        square()
    except rospy.ROSInterruptException:
        pass      