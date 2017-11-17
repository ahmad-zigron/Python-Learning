# Q: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

try:
	values=[x for x in raw_input("Enter Words to Sort with comma__").split(',')]
	values.sort()
	print "Sorted Values__",','.join(values)	
except:
	print"Values Not looking good "
