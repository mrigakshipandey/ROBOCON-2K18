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
def reach(x):
    	rospy.wait_for_service('destination')
    	attempt_algo = rospy.ServiceProxy('destination', general)
    	success = attempt_algo(x)
    	if success.y=='1':
		print "Reached %s "%x

def manual():
    	rospy.wait_for_service('manual_present')
    	attempt_algo = rospy.ServiceProxy('manual_present', general)
    	success = attempt_algo('1')
	if success.y=='1':
		print "manual Present"
	else:
		print "manual not present"
    	return success.y

def gball():
    	rospy.wait_for_service('count_gball')
    	attempt_algo = rospy.ServiceProxy('count_gball', general)
    	success = attempt_algo('1')
	print "No of normal golden balls left = %s "%success.y
    	return success.y

def totalgball():
    	rospy.wait_for_service('read_total_gball')
    	attempt_algo = rospy.ServiceProxy('read_total_gball', general)
    	success = attempt_algo('1')
    	return success.y

def loadrack():
    	rospy.wait_for_service('load_rack_action')
    	attempt_algo = rospy.ServiceProxy('load_rack_action', general)
    	success = attempt_algo('1')
	if success.y=='1':
		print "Rack Loaded Successfully"
    	return success.y

def Read_state():
    	rospy.wait_for_service('know')
    	attempt_algo = rospy.ServiceProxy('know', general)
    	success = attempt_algo('1')
    	return success.y

def rack():
    	rospy.wait_for_service('rack_present')
    	attempt_algo = rospy.ServiceProxy('rack_present', general)
    	success = attempt_algo('1')
    	if success.y=='1':
		print "Rack Present"
	else:
		print "Rack not present"
	return success.y

def golden_throw():
    	rospy.wait_for_service('gthrow_action')
    	attempt_algo = rospy.ServiceProxy('gthrow_action', general)
    	success = attempt_algo('1')
    	if success.y=='1':
		print "Rong Bay Throw Action Successful"

def handle(resp):
	if manual()=='1':
		if(gball()=='0'):
			Write('4')
			print "No Rong bay..."
			return generalResponse('0')
		else:
			if rack()=='0':
				reach('5')
				loadrack()

	else:
		if gball()=='0':
			Write('3')
			print "RONG BAY"
			return generalResponse('0')
		elif gball()==totalgball():
			print "Waiting for manual"
			return generalResponse('0')
		else:
			if rack=='0':
				print "LOST RACK"
				return generalResponse('0')

	reach('3')
	if golden_throw()=='1':
		print "all 5 golden balls released..."
		return generalResponse('1')
	else:
		print "Something went wrong..."
		return generalResponse('0')
		

def Go():
	rospy.init_node('rb_throw')
	s = rospy.Service('rb_time', general, handle) #Service Name, CMakeList File, Call
    	rospy.spin()
	


##################################################################
#Main Program
##################################################################

if __name__ == '__main__':
    Go()
