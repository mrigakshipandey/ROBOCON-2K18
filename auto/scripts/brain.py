#!/usr/bin/env python

##################################################################
# Import Libraries
##################################################################

import rospy
from subprocess import call
import sys


##################################################################
# Messages ans Services used
##################################################################

from auto.srv import *


##################################################################
# Function Definitions
##################################################################

def terminate():
    	sys.exit(0)

def Normal_throw(x):
    	rospy.wait_for_service('throw_from')
    	attempt_algo = rospy.ServiceProxy('throw_from', general)
    	success = attempt_algo(x)
    	if success.y=='1':
		print "BALL PASSED THE HOOP from %s "%x

def Throw_RB():
    	rospy.wait_for_service('rb_time')
    	attempt_algo = rospy.ServiceProxy('rb_time', general)
    	success = attempt_algo('1')
    	if success.y=='1':
		print "Rong Bay"


def reach(x):
    	rospy.wait_for_service('destination')
    	attempt_algo = rospy.ServiceProxy('destination', general)
    	success = attempt_algo(x)
    	if success.y=='1':
		print "Reached %s "%x
	      
def Read_state():
	print "Read function called"
    	rospy.wait_for_service('know')
    	attempt_algo = rospy.ServiceProxy('know', general)
    	success = attempt_algo('1')
    	return success.y
	
def Write(x):
    	rospy.wait_for_service('update')
    	attempt_algo = rospy.ServiceProxy('update', general)
    	success = attempt_algo(x)
    	if success.y=='1':
		print "New State %s"%x

def overwrite():
    	rospy.wait_for_service('overwrite')
    	attempt_algo = rospy.ServiceProxy('overwrite', general)
    	success = attempt_algo('1')


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    try:
	print "Starting ..."
	rospy.init_node('Brain')
	

        while True:
		
		s=Read_state()
		print "State = %s"%s
	
        	if (s=='3' or s=='5'): terminate()

        	elif(s=='0' or s=='1'): Normal_throw(str(int(s)+1))#From Throw position TZ s+1

        	else:
            		reach('5')#Reach load position TZ2
            		if(s=='2'):
                		Throw_RB()
            		if(s=='4'):
                		Normal_throw('2') #Make sure state change does not happen
	
		
    except rospy.ROSInterruptException:
        pass

