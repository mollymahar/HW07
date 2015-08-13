# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# body
def nested_sum(l, sum=0.0):
	"""This function takes a list composed of nested lists and returns the sum as a float."""
	for item in l:
		if type(item) == type([]): 				# use recursion if the item is a list
			sum = nested_sum(item, sum)
		else:
			sum += item							# just add to the sum if item is a number
	return sum



# call the main function
def main():
	pass

if __name__ == '__main__':
	main()