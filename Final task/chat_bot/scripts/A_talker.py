#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.33)
    while not rospy.is_shutdown():
        str1 = "hey man"
        rospy.loginfo(str1)
        pub.publish(str1)
        rate.sleep()

        str2 = "how are you bro?"
        rospy.loginfo(str2)
        pub.publish(str2)
        rate.sleep()

        str3 = "fine man"
        rospy.loginfo(str3)
        pub.publish(str3)
        rate.sleep()

        str4 = "Nice to meet you man"
        rospy.loginfo(str4)
        pub.publish(str4)
        rate.sleep()

        str5 = "Bye man"
        rospy.loginfo(str5)
        pub.publish(str5)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
