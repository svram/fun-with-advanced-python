# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
	Simple demo of how local and global scope works in python
	
	Usage: Open the command line and type:
		$ python scope.py
	Then follow the output along with the code comments to understand what's going on
	
	© 2017 Vikram Bahl
'''


def simple_local_scope(a):
	print "x = {}".format(x)
	print "a = {}".format(a)

def call_before_assignment(a):
	print "a = {}".format(a)
	try:
		print "z = {}".format(z)
	except NameError:
		
		print "There is no 'z'. Define it first. "

def define_local_variable(a):
	x = 22
	print "x = {}".format(x)
	print "a = {}".format(a)

def access_local_variable_before_definition(a):
	
	try:
		print "x = {}".format(x)
	except UnboundLocalError:
		print "UnboundLocalError: local variable 'x' referenced before assignment"

	x = 2000
	print "x = {}".format(x)
	print "a = {}".format(a)

def global_scope(a):
	global x
	print "x = {}".format(x)
	x = "X has changed"
	print "x = {}".format(x)
	print "a = {}".format(a)

def global_vs_local(a, b):
	global x
	print "x = {}".format(x)
	print "a = {}".format(a)
	b = "New Value for B"
	print "b = {}".format(b)

	

if __name__ == '__main__':
	#The program execution begins here.
	
	'''
		We are defining x = 10 before calling the function. The function
		simple_local_scope(a) sees that x is defined outside the function.
	'''
	x = 10
	simple_local_scope(200)
	print "x = {}".format(x)

	print("----------------------------")

	'''
		In this example, we are accessing the variable 'z' before assigning it.
		When the python interpretor sees a variable that hasn't been declared in before,
		it will throw a 'NameError'. If you remove the try...except block and run the,
		program again, the interpretor will throw an error:
		NameError: global name 'z' is not defined
	'''

	call_before_assignment(200)

	print("----------------------------")

	'''
		In this case we assign the variable z before it is accessed in the function call_before_assignment
	'''
	z = 50
	call_before_assignment(200)

	print("----------------------------")

	'''
		Here, we assign x = 22 in the function define_local_variable. The interpretor treats that x as being
		differnt from the other 'global' x which was equal to 1000. The interpretor see the x=22 being local
		in scope. However, after the function call returns to main, it prints x = 1000 since this x is
		global in scope for the program concerned.
	'''

	x = 1000
	define_local_variable(200)
	print "x = {}".format(x)

	print("----------------------------")

	'''
		This is where it gets a little tricky. Notice that in the function access_local_variable_before_definition,
		we are trying to print x before assigning it locally to the value 2000. The interpretor scans the entire
		function and sees that x is being assigned. It treats it as a local variable for that function. Since it treats
		x as a local variable, it cannot be printed before it is assigned. Note that there is no NameError thrown since
		the interpretor already knows about x. Once the program exits to main it prints x = 10 as expected.
	'''

	x = 10
	access_local_variable_before_definition(200)
	print "x = {}".format(x)

	print("----------------------------")

	'''
		Lets look at the global scope. In the function global_scope(a), we use the 'global' keyword to tell the interpretor
		to use the value of x defined outside the function. x=25 before the function was called. However, we assigned x = "X has changed"
		within the function. This changed the value of the global x. This is seen by the print statement after the function is called.

		DO NOTE THAT IT IS NOT PYTHONIC TO CHANGE THE VALUE OF A GLOBAL VARIABLE INSIDE A FUNCTION AS IT MAKES DEBUGGING HARDER
	'''

	x = 25
	global_scope(200)
	print "x = {}".format(x)

	print("----------------------------")

	'''
		This example lets us see the difference between global and local variables. Note that b is a global variable
		outside the global_vs_local function but is a local variable within the function. Thats why its value doesnt change 
		in the print statemtn after the function is called
	'''
	x = 1000
	b = 2500
	global_vs_local(200, 2500)
	print "x = {}".format(x)
	print "b = {}".format(b)
