# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Returns ['Apple', ['Bear'], 'Cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# body
def capitalize_nested(l):
	"""This function takes a nested list of strings/words and capitalizes the first letter of each string.
	It returns a list that may also have nested elements within."""
	for i in range(0, len(l)):
		if type(l[i]) == type([]):
			capitalize_nested(l[i]) 				# use recursion if interior item is a list
		else:	
			l[i] = l[i].capitalize() 				# otherwise we can just capitalize the string
	return l



# call main + boilerplate
def main():
	pass

if __name__ == '__main__':
	main()
