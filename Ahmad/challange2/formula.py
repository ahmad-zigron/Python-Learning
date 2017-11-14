print("Find Q = Square Root of[(2*C*D)/H] Where C= 50, H=30")
while True:
	try:	
		import math
		c=50
		h=30
		value = []
		items=[x for x in raw_input("Enter A Value of D__").split(',')]
		for d in items:
		    value.append(str(int(math.sqrt(2*c*float(d)/h))))

		print ("Value of Q ="),','.join(value)
		break
		
	except:
		print"Sorry! Please Enter an Integer"
		continue
#print(math.__doc__)
