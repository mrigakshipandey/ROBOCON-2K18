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

def handle(resp):
	print "Checking Ball..."
	if np.random.rand(1)>0.5:
		return generalResponse('1')
		
	else:
		return generalResponse('0')
		

def random_result():
	rospy.init_node('check_ball')
	s = rospy.Service('ball_present', general, handle) #Service Name, CMakeList File, Call
    	rospy.spin()
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    random_result()
