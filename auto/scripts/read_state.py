#!/usr/bin/env python
import rospy
from auto.srv import *
import re

def Read(resp):
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'r+')
		# read 1 line from the end, return the value
    		a=file.read()
		file.close()
		wordList=re.sub("[^\w]"," ",a).split()
		ab=wordList[-1]
		return generalResponse(ab)
	
	except IOError:
		file=open('/home/ubuntu/catkin_ws/src/auto/files/state.txt', 'a+')
		file.write('\n0')
		file.close()
		return generalResponse('0')
 
if __name__ == '__main__':
    	rospy.init_node('Read_State')
    	rospy.Service('know', general, Read) 
	rospy.spin()
