#!/usr/bin/env python
import rospy
from auto.srv import *
import re

#reads the file, appends ball--

#####################################################################
#Function definition
#####################################################################

def totalball():
    	rospy.wait_for_service('read_gtotal_ball')
    	attempt_algo = rospy.ServiceProxy('read_gtotal_ball', general)
    	success = attempt_algo('1')
    	return success.y

def Write(resp):
	try:
    		file = open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'r+')
		# read 1 line from the end
    		a=file.read()
		file.close()
		wordList=re.sub("[^\w]"," ",a).split()
		ab=wordList[-1]
		
		# append ab-1
		file = open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'a+')
    		c = file.write('\n%s'%str(int(ab)-1))
		file.close()
		return generalResponse(str(int(ab)-1))
  
	
	except IOError:
		file=open('/home/ubuntu/catkin_ws/src/auto/files/gball.txt', 'a+')
		file.write('\n%s'%str(int(totalball())-1))
		file.close()
		
    	  	return generalResponse(str(int(totalball())-1))

####################################################################
#Main Program
####################################################################
 
if __name__ == '__main__':
    	rospy.init_node('Update_GBall')
    	rospy.Service('update_gball', general, Write) 
	rospy.spin()
