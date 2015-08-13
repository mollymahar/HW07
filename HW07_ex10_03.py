# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# body
def cumulative_sum(l):
	"""This function takes a list of integers and returns the cumulative sum at each index.
	It returns a list."""
	for i in range(1, len(l)):
		l[i] = l[i] + l[i-1]
	return l



# call main function
def main():
	pass

if __name__ == '__main__':
	main()