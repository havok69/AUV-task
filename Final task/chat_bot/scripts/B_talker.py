#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.3)
    while not rospy.is_shutdown():
        str1 = "hey bro"
        rospy.loginfo(str1)
        pub.publish(str1)
        rate.sleep()

        str2 = "Fine bro"
        rospy.loginfo(str2)
        pub.publish(str2)
        rate.sleep()

        str3 = "How about you bro?"
        rospy.loginfo(str3)
        pub.publish(str3)
        rate.sleep()

        str4 = "Nice meeting you too bro"
        rospy.loginfo(str4)
        pub.publish(str4)
        rate.sleep()

        str5 = "Bye bro"
        rospy.loginfo(str5)
        pub.publish(str5)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

