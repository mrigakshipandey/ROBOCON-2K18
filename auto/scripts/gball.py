#!/usr/bin/env python
import rospy
from auto.srv import *


def totalgball():
    	rospy.wait_for_service('read_gtotal_ball')
    	attempt_algo = rospy.ServiceProxy('read_gtotal_ball', general)
    	success = attempt_algo('1')
    	return success.y

def Read(resp):
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'r+')
		# read 1 line from the end, return the value
    		a=file.readlines()
		file.close()
		ab=a[-1]
		return generalResponse(ab)
	
	except IOError:
		file=open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'a+')
		file.write('\n%s'%totalgball())
		file.close()
		return generalResponse(totalgball())
 
if __name__ == '__main__':
    	rospy.init_node('GBall_Counter')
    	rospy.Service('count_gball', general, Read) 
	rospy.spin()
