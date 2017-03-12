import argparse

def get_args():

	parser = argparse.ArgumentParser(description="simple argument parser",
									epilog="This is an example usage case")
	parser.add_argument('-x', action="store", required=True, help="Help text for X")
	print parser.parse_args()


if __name__ == '__main__':
	get_args()