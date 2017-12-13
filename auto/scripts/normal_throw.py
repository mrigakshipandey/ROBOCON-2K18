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

def Throw_Arm_Activate():
    	rospy.wait_for_service('throw_action')
    	attempt_algo = rospy.ServiceProxy('throw_action', general)
    	success = attempt_algo('1')
    	if success.y=='1':
		print "Throw Action Successful"

def checkball():
    	rospy.wait_for_service('ball_present')
    	attempt_algo = rospy.ServiceProxy('ball_present', general)
    	success = attempt_algo('1')
    	if success.y=='1':
		print "Ball Present"
	else:
		print "Ball not present"
	return success.y

def reach(x):
    	rospy.wait_for_service('destination')
    	attempt_algo = rospy.ServiceProxy('destination', general)
    	success = attempt_algo(x)
    	if success.y=='1':
		print "Reached %s "%x

def Update_ball():
    	rospy.wait_for_service('update_ball')
    	attempt_algo = rospy.ServiceProxy('update_ball', general)
    	success = attempt_algo('1')
	print "One Ball deducted..."
    
def manual():
    	rospy.wait_for_service('manual_present')
    	attempt_algo = rospy.ServiceProxy('manual_present', general)
    	success = attempt_algo('1')
	if success.y=='1':
		print "manual Present"
	else:
		print "manual not present"
    	return success.y

def ball():
    	rospy.wait_for_service('count_ball')
    	attempt_algo = rospy.ServiceProxy('count_ball', general)
    	success = attempt_algo('1')
	print "No of normal balls left = %s "%success.y
    	return success.y


def Write(x):
    	rospy.wait_for_service('update')
    	attempt_algo = rospy.ServiceProxy('update', general)
    	success = attempt_algo(x)
    	if success.y:
		print "New State %s"%x

def loadball():
    	rospy.wait_for_service('load_ball_action')
    	attempt_algo = rospy.ServiceProxy('load_ball_action', general)
    	success = attempt_algo('1')
	if success.y=='1':
		print "Ball Loaded Successfully"
    	return success.y

def Read_state():
    	rospy.wait_for_service('know')
    	attempt_algo = rospy.ServiceProxy('know', general)
    	success = attempt_algo('1')
    	return success.y

def totalball():
    	rospy.wait_for_service('read_total_ball')
    	attempt_algo = rospy.ServiceProxy('read_total_ball', general)
    	success = attempt_algo('1')
    	return success.y
#also in update ball

def handle(resp):
	print "Attempting Throw..."
	reach(resp.x)
	if(checkball()=='1'):
		Throw_Arm_Activate()
		Update_ball()
		if(ball()=='0'):
			Write('5')
	else:
		if(manual()=='1'):
			reach(str(int(resp.x)+3))
			loadball()
		else:
			if not((ball()==totalball()) or (Read_state()=='4')):
				print "Updating state"
				Write(resp.x)
				return generalResponse('1')
			else:
				print "No Action Taken Waiting for manaual or State = 4"
	return generalResponse('0')

def go():
	rospy.init_node('normal_throw')
	s = rospy.Service('throw_from', general, handle) #Service Name, CMakeList File, Call
    	rospy.spin()
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    go()
