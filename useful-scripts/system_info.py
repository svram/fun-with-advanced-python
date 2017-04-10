# -*- coding: utf-8 -*- 
#!/usr/bin/env python 
 
''' 
 		Useful function stubs to retrieve information about your OS, hardware, network connection.
 		The commands are pretty straightforward and function calls are self-explanatory.
 		Check out the documentation for the os, sys and platfirm modules:
 			https://docs.python.org
 
		© 2017 Vikram Bahl 
'''

import os, sys, platform

def get_machine_info():
	
	print "MACHINE TYPE: {}".format(platform.machine())
	print "PLATFORM: {}".format(platform.platform(aliased=True, terse=False))
	print "PROCESSOR: {}".format(platform.processor())

if __name__ == '__main__':
	get_machine_info()