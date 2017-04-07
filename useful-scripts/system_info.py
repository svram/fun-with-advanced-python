# -*- coding: utf-8 -*- 
#!/usr/bin/env python 
 
''' 
 		Useful function stubs to retirive information about your OS, hardware, network connection etc
 
		© 2017 Vikram Bahl 
'''

import os, sys, platform

def get_machine_info():
	print platform.machine()

if __name__ == '__main__':
	get_machine_info()