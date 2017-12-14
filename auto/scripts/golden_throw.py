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

def Update_gball():
    	rospy.wait_for_service('update_gball')
    	attempt_algo = rospy.ServiceProxy('update_gball', general)
    	success = attempt_algo('1')
	print "One Golden Ball deducted..."

def handle(resp):
	print "Throwing All 5 golden balls..."
	x=0
	while x<5:
		Update_gball()
		x+=1

	return generalResponse('1')

def random_result():
	rospy.init_node('golden_throw')
	s = rospy.Service('gthrow_action', general, handle) #Service Name, CMakeList File, Call
    	
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    	random_result()
	rospy.spin()
