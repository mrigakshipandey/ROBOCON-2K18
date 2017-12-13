#!/usr/bin/env python
import rospy
from auto.srv import *


def totalball():
    	rospy.wait_for_service('read_total_ball')
    	attempt_algo = rospy.ServiceProxy('read_total_ball', general)
    	success = attempt_algo('1')
    	return success.y

def Read(resp):
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/ball.txt', 'r+')
		# read 1 line from the end, return the value
    		a=file.readlines()
		file.close()
		ab=a[-1]
		return generalResponse(ab)
	
	except IOError:
		file=open('/home/ubuntu/catkin_ws/src/auto/files/ball.txt', 'a+')
		file.write('\n%s'%totalball())
		file.close()
		return generalResponse(totalball())
 
if __name__ == '__main__':
    	rospy.init_node('Ball_Counter')
    	rospy.Service('count_ball', general, Read) 
	rospy.spin()
