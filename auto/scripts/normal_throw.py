#!/usr/bin/env python

##################################################################
# Import Libraries
##################################################################

import rospy
import numpy as np


##################################################################
# Messages ans Services used
##################################################################

from auto.srv import *


##################################################################
# Function Definitions
##################################################################

def Write(x):
    	rospy.wait_for_service('update')
    	attempt_algo = rospy.ServiceProxy('update', general)
    	success = attempt_algo(x)
    	if success.y:
		print "New State %s"%x

def Read_state():
    	rospy.wait_for_service('know')
    	attempt_algo = rospy.ServiceProxy('know', general)
    	success = attempt_algo('1')
    	return success.y

def handle(resp):
	print "Attempting Throw..."
	if np.random.rand(1)>0.5:
		
		# update state if not equal to 4
		if (not Read_state()=='4'): Write(str(int(Read_state())+1))
		return generalResponse('1')
	else:
		return generalResponse('0')

def random_result():
	rospy.init_node('normal_throw')
	s = rospy.Service('throw_from', general, handle) #Service Name, CMakeList File, Call
    	rospy.spin()
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    random_result()
