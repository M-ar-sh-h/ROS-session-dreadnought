#!/usr/bin/python3

import rospy # Importing the ROS client library for python
from std_msgs.msg import String # Importing the String message type

def callback(data): 
    # Declaring a callback function. data is the message we receive from the publisher
    print(f"I saw {data.data}") # Printing it to console
    
def viewer():
    rospy.init_node('sachin', anonymous=True) # Intitializing the node
    rospy.Subscriber('vines', String, callback) # Subscribing to a topic
    rospy.spin() # keeps your node from exiting until the node has been shutdown

if __name__ == '__main__':
    viewer()
