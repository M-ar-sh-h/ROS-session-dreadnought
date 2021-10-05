#!/usr/bin/python3

import rospy # Importing the ROS client library for python
from std_msgs.msg import String # Importing the String message type

def publish_video():
    pub = rospy.Publisher('vines', String, queue_size=1) # Subscribing to a topic
    rospy.init_node('carryminati', anonymous=True) # Intitializing the node
    rate = rospy.Rate(1) # Frequency of sent messages. Here 1 means 1Hz
    iteration = 1
    while not rospy.is_shutdown(): 
        video = f"Carry's video number {iteration}" 
        pub.publish(video) # Publishing the message
        print(video)
        iteration += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_video()
    except rospy.ROSInterruptException:
        pass
