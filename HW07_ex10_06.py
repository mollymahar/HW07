# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#body
def is_sorted(l):
	"""This function takes a list and checks whether or not it is sorted."""
	for i in range(1, len(l)):
		try:
			if l[i].lower() <= l[i-1].lower(): 			# ignore upper/lowercase with strings
				return False
		except: 										# if not strings
			if l[i] <= l[i-1]:
				return False
	return True


# call main function
def main():
	pass

if __name__ == '__main__':
	main()