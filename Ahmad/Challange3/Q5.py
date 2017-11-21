#Quetion 5:
#Use a list comprehension to square each odd number in a list. The list is input by a sequence of #comma-separated numbers.
#Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,3,5,7,9
while True:
	try:
		values = raw_input("Enter Comma Seperatsssed Input__:")
		numbers = [x for x in values.split(",") if int(x)%2!=0]
		print "Odd Numbers are__:",",".join(numbers)
		break
	except:
		print("Sorry Try Again! & Put only Integers Don't Use Foating Numbers")
		continue
