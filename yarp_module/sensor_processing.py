#!/usr/bin/python3

import configparser
import yarp
import sys
import os
import subprocess


config_name = "config2.ini"
# class DataProcessor(yarp.BottleCallback):
#     def onRead(self, bot, *args, **kwargs):
#         # print('Bottle [%s], args [%s], kwargs [%s]' % \)
#         (bot.toString(), args, kwargs) 


# class DataPort(yarp.BufferedPortBottle):
#     def onRead(self,connection):
#         if not(connection.isValid()):
#             print("Connection shutting down")
#             return False
#         bin = yarp.Bottle()
#         bout = yarp.Bottle()
#         ok = bin.read(connection)
#         if not(ok):
#             print("Failed to read input")
#             return False
#         print("%s"%bin.toString())
#         bout.addString("Received:")
#         bout.append(bin)
#         print("Sending [%s]"%bout.toString())
#         writer = connection.getWriter()
#         if writer==None:
#             print("No one to reply to")
#             return True
#         return bout.write(writer)

# def open_port(name_port):
# 	"""
# 	Open a buffered port for the name in input
# 	"""
# 	p = yarp.BufferedPortBottle()
# 	p.open(name_port);
# 	return p


# def close_port(port):
# 	port.close()



if __name__=="__main__":
	try:
		yarp.Network.init()
	

		rf = yarp.ResourceFinder()
		rf.setVerbose(True);
		rf.setDefaultContext("myContext");
		rf.setDefaultConfigFile("config2.ini");
		rf.configure(sys.argv)


		config = configparser.ConfigParser()
		config.read(config_name)
		sections = config.sections()
		section = sections[0]
		name_port = config[section]['port']
		name = '/processing' + str(name_port) + ':i'

		print("test")
		subprocess.Popen(["/home/amalaise/Documents/These/code/activity-recognition-prediction-wearable/yarp_module/rf_module.py", name])

		# while(1):
		# 	try:
		# 		yarp.Time.delay(0.01)

		except KeyboardInterrupt:
			break

	finally:

		yarp.Network.fini()