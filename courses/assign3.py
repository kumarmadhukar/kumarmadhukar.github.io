import sys

# Do not change the name of the function. 
# Do not use global variables as we will run your code on 
# test cases.
# 
def solve(inputString, n):
	#
	# Write your code here
	#
	return "nil"


# Main function: do NOT change this.
if __name__=="__main__":
	inputFile = sys.argv[1]
	n = int(sys.argv[2])
	with open(inputFile, 'r') as f:
		inputString = f.read()
		print(solve(inputString, n))