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

def totalgball():
	#print "Total gball called"
    	rospy.wait_for_service('read_total_gball')
    	attempt_algo = rospy.ServiceProxy('read_total_gball', general)
    	success = attempt_algo('1')
    	return success.y

def OverWrite():
	print "Inside OverWrite Server"
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'r+')
		file.seek(0)
		file.truncate()
		file.write('\n0')
		file.close()
		print "State.txt ready"		
		
		file = open('/home/ubuntu/catkin_ws/src/auto/files/ball.txt', 'r+')
		file.seek(0)
		file.truncate()
		file.write('\n%s'%totalball())
		file.close()
		print "ball.txt ready"

		file = open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'r+')
		file.seek(0)
		file.truncate()
		#print "file emptied"
		file.write('\n%s'%totalgball())
		print "gball.txt ready"
		file.close()
		
		return generalResponse('1')
			
	except IOError:
		print "************************************************************IOError occured"
 
if __name__ == '__main__':
    	rospy.init_node('Over_Write')
    	OverWrite()
	rospy.spin()
