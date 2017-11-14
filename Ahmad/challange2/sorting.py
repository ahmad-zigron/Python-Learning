try:
	values=[x for x in raw_input("Enter Words to Sort with comma__").split(',')]
	values.sort()
	print "Sorted Values__",','.join(values)	
except:
	print"Values Not looking good "
