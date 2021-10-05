# ROS Session

**By** - Mookesh Dash

------

ROS programmes work in the form of **_nodes_**

Now what are nodes?

Let's understand it with a simple example...

![Screenshot-20210828013634-600x313](/images/Screenshot-20210828013634-600x313.png)

- **Sachin** and **Carryminati** are two users signed in to **Youtube**.
- **Sachin** wants to receive **Carryminati**'s videos in his feed and therefore, he **_subscribes_** to **Carryminati**.
- Now **Carryminati** **_publishes_** the video so that **Sachin**, who has subscribed to him can watch it.
- Therefore,
  - **Sachin** is a **_subscriber_**,
  - **Carryminati** is a **_publisher_** , and,
  - **YouTube** is the medium which allows them to communicate.

Now coming to ROS terms,

- **_rosnode_** - Sachin & Carryminati. The publishers and subscribers. They are programmes running inside ROS.
- **_roscore_** - YouTube. The medium that allows nodes to communicate. We can call it the master node which every node registers itself to.
- **_rostopic_** - Vines. The topic on which two nodes communicate.
- **_rosmsg_** - Video or '.mp4'. The type of message communicated between the nodes.

Enough talk! Let's see a real pubsub programme...

First we have to initialize the **_roscore_**, so that nodes can communicate.

```bash
$ roscore
```

Go into your **catkin_ws**, scripts folder and create a new package.

```bash
$ cd ~/catkin_ws/src
$ catkin_create_pkg pubsub std_msgs rospy roscpp
```

```catkin_create_pkg``` creates a package named **pubsub** that depends on **_std_msgs_**, **_rospy_** and **_roscpp_**.

Then, we have to build the packages in the **catkin_ws** and source the generated setup file to add our workspace to the ROS environment.

```bash
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
```

Make a script folder, (I have named it **src**) inside your **pubsub** package and move into it. Create two python files named _carry.py_ and _sachin.py_

```bash
$ cd src/pubsub/
$ cd src/
$ touch carry.py sachin.py
```

Open your _carry.py_ file in a text editor, and paste the following code:-

```python
# Add your python interpreter path in the next line
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
        iteration += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_video()
    except rospy.ROSInterruptException:
        pass

```

Next open your _sachin.py_ file in a text editor, and paste the following code:-

```python
# Add your python interpreter path in the next line
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
```

Save both the files, and in your bash make both the files executable by running:-

```bash
$ chmod +x carry.py sachin.py
```

Now go back to your **catkin_ws** and build your packages again.

```bash
$ cd ~/catkin_ws && catkin_make && source devel/setup.bash
```

Next, run your scripts using

```bash
$ rosrun pubsub carry.py
$ rosrun pubsub sachin.py
```

Our nodes are up and running!

<video src="/videos/example_node.mp4"></video>

Let's inspect our _nodes_ and _topics_...

```bash
$ rosnode list
$ rostopic list
```

![rosseshss](/images/rosseshss.png)

There's a nice way to check how the **nodes** and **topics** are working in a graphical way

```bash
$ rosrun rqt_graph rqt_graph
```

​                ![rosseshrqt](/images/rosseshrqt.png)

And indeed! **_carryminati_** and **_sachin_** are our two **nodes**, and the **topic** they are interacting with each other on is about **_vines_**.

That's it for today's sesh. I hope y'all have understood how **nodes** interact with each other via **topics** and if any doubts at all feel free to contact me anytime!
