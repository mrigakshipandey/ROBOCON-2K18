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
	print "Loading Ball..."
	return generalResponse('1')

def random_result():
	rospy.init_node('load_ball')
	s = rospy.Service('load_ball_action', general, handle) #Service Name, CMakeList File, Call
    	
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    	random_result()
	rospy.spin()
