#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import String

def callback_order(data):

    global cero
    global one
    global two

    order=String()
    order=data.data

    if order == 'go home':
        cero=0
        one=0
        two=0
    elif order == 'stand up':
        cero=0
        one=90
        two=0
    elif order == 'say hello':
        cero=45
        one=45
        two=45
    elif order == 'sky':
        cero=20
        one=20
        two=20
    elif order == 'dog':
        cero=60
        one=60
        two=60
    elif order == 'cat':
        cero=40
        two=40
        three=40

def node():

    global cero
    global one
    global two

    cero=UInt16()
    one=UInt16()
    two=UInt16()

    rospy.init_node('robot_rover_package',anonymous=True)

    rospy.Subscriber("recognizer/output",String,callback_order)

    #Publisher to 3 servos

    servo0_pub=rospy.Publisher('servo0',UInt16,queue_size=10)
    servo1_pub=rospy.Publisher('servo1',UInt16,queue_size=10)
    servo2_pub=rospy.Publisher('servo2',UInt16,queue_size=10)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        servo0_pub.publish(cero)
        servo1_pub.publish(one)
        servo2_pub.publish(two)
        rate.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
