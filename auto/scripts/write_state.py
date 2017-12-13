#!/usr/bin/env python
import rospy
from auto.srv import *

def Write(resp):
    	file = open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'a+')
    	c = file.write('\n%s'%resp.x)
	file.close()
    	return generalResponse('1')
 
if __name__ == '__main__':
    	rospy.init_node('Write_State')
    	rospy.Service('update', general, Write) 
	rospy.spin()
