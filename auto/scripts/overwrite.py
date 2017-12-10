#!/usr/bin/env python
import rospy
from auto.srv import *
import re
import sys

def OverWrite():
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'r+')
		# read 1 line from the end, return the value
		file.seek(0)
		file.truncate()
		file.write('\n0')
		file.close()
		sys.exit()
	
	except IOError:
		pass
 
if __name__ == '__main__':
    	rospy.init_node('Over_Write')
    	OverWrite()
	rospy.spin()
