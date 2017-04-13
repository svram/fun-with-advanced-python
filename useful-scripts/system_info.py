# -*- coding: utf-8 -*- 
#!/usr/bin/env python 
 
''' 
 		Useful function stubs to retrieve information about your OS, hardware.
 		The commands are pretty straightforward and function calls are self-explanatory.

 		I will be adding to this as time goes on, but if you are familiar with the command line,
 		then you can do it easily from there without the overhead. 
 		
 		Check out the documentation for the os, sys and platfirm modules:
 			https://docs.python.org
 
		© 2017 Vikram Bahl 
'''

import os, sys, platform

def get_machine_info():
	
	print "-----------------------PLATFORM INFORMATION-----------------------\n"
	print "MACHINE TYPE: {}".format(platform.machine())
	print "PLATFORM ARCHITECTURE: {}".format(platform.architecture())
	print "PLATFORM: {}".format(platform.platform(aliased=True, terse=False))
	print "PROCESSOR: {}".format(platform.processor())
	print "COMPUTER NAME: {}".format(platform.node())
	print "PYTHON VERSION: {}".format(sys.version)
	
	#Note: You can get all the information above by running platform.uname() which returns a tuple of strings
	#print platform.uname()

	print "BYTE ORDER: {}".format(sys.byteorder) + " endian"


'''
	Function to test if platform is Windows
'''
def isWindows():
	return any(platform.win32_ver())

if __name__ == '__main__':
	get_machine_info()