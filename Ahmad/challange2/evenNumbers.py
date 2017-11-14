print("Enter Range to find Even numbers between")
while True:
 try:		
		a = input("Enter 1st Value__")
		b = input("Enter 2nd Value__")
		values = []
		for i in range(a, b):
			if (i%2==0): 
			    values.append(str(i))
		print (",".join(values))
		break
	except:
		print"Please Enter Exact Integers range "
		continue
