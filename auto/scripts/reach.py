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
	print "Travelling..."
	return generalResponse('1')

def random_result():
	rospy.init_node('reach')
	s = rospy.Service('destination', general, handle) #Service Name, CMakeList File, Call
    	
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    	random_result()
	rospy.spin()
