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
	print "Throw Arm Activated..."
	return generalResponse('1')

def random_result():
	rospy.init_node('Throw_Arm')
	s = rospy.Service('throw_action', general, handle) #Service Name, CMakeList File, Call
    	
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    	random_result()
	rospy.spin()
