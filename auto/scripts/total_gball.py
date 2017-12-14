#!/usr/bin/env python
import rospy
from auto.srv import *
import re

def Read(resp):
	try:
    		print "Inside total gball server"
		file = open('/home/ubuntu/catkin_ws/src/auto/files/global.txt', 'r+')
		# read 1 line from the end, return the value
    		a=file.readlines()
		file.close()
		a=a[-1]
		#print a
		wordList=re.sub("[^\w]"," ",a).split()
		#print wordList
		ab=wordList[1]
		#print ab
		return generalResponse(ab)
	
	except IOError:
		print "Golbal file does not exist"
		return generalResponse('0')
 
if __name__ == '__main__':
    	rospy.init_node('global_gball')
    	rospy.Service('read_total_gball', general, Read) 
	rospy.spin()
