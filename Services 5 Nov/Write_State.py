#!/usr/bin/env python
import rospy
from robocon18.srv import general

def Write(x):
    file = open('state.txt', 'a+')
    c = file.write(x.data)
    return generalResponse(c)
 
if __name__ == '__main__':
    rospy.init_node('Write_State')
    rospy.Service('update', general, Write)   