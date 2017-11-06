#!/usr/bin/env python
import rospy
from robocon18.srv import general

def manual_check_sen

def Go(x):
    found=manual_check_sensors()
    return generalResponse(found)
 
if __name__ == '__main__':
    rospy.init_node('Check_Manual')
    rospy.Service('manual_present', general, Go)