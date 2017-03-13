'''
	Simple demo with the argparse module

	Usage: open the command line and run the program with the option as listed in
		   the function get_args(): 

		   $ python arg_demo.py -h
'''

import argparse

def get_args():

	#initializing the parser with a description of what it does
	parser = argparse.ArgumentParser(description="simple argument parser",
									epilog="This is an example usage case")
	#required arguments go here
	# the '--execute' is the long option. The result stores the valu in 'execute'. Either -x or --execute can be used
	parser.add_argument('-x', '--execute', action="store", required=True, help="Help text for option X")

	#optional arguments
	
	parser.add_argument('-y', default="False", help="Help text for option Y")
	parser.add_argument('-z', type=int, help="Help text for option Z. This must be an integer.")

	#test on the command line with different option values to see result
	'''
	$ python arg_demo.py -x "x value" -z 11 -y "y value" should give the result:
	$ Namespace(execute='x value', y='y value', z=11)
	'''

	'''
	Lets create a mutually exclusive group for 2 arguments -position and -momentum.
	This means that the program will throw an error if both -yin and -yang options are provided as input.
	Possible use case: Let's say we are modelling Heisenbergs principle. We cannot provide a position AND momentum
					   for an atomic particle at the same time as it would be a violation of the principle
	'''

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-p', '--position', help="The position of the atomic particle")
	group.add_argument('-m', '--momentum', help="The position of the atomic particle")

	#run the program with both options and see the result

	print parser.parse_args()


if __name__ == '__main__':
	get_args()