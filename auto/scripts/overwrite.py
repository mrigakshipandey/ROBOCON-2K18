#!/usr/bin/env python
import rospy
from auto.srv import *
import re
import sys

#overwrite the ball.txt with totalball()

def totalball():
    	rospy.wait_for_service('read_total_ball')
    	attempt_algo = rospy.ServiceProxy('read_total_ball', general)
    	success = attempt_algo('1')
    	return success.y

def OverWrite():
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'r+')
		# read 1 line from the end, return the value
		file.seek(0)
		file.truncate()
		file.write('\n0')
		file.close()
		
		
		file = open('/home/ubuntu/catkin_ws/src/auto/files/ball.txt', 'r+')
		# read 1 line from the end, return the value
		file.seek(0)
		file.truncate()
		file.write('\n%s'%totalball())
		file.close()
		
		sys.exit()
			
	except IOError:
		pass
 
if __name__ == '__main__':
    	rospy.init_node('Over_Write')
    	OverWrite()
	rospy.spin()
