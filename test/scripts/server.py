#!/usr/bin/env python

from test.srv import * #package name.srv
import rospy

def handle(req):
	# The test algo goes here
	c=str(int(req.x) + 3)
	print "Returning %s"%c
    	return generalResponse(c)

def add_two_ints_server():
    	rospy.init_node('server')
    	s = rospy.Service('sample', general, handle) #Service Name, CMakeList File, Call
    	print "Server Ready."
    	rospy.spin()

if __name__ == "__main__":
    	add_two_ints_server()


