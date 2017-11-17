# Q: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

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
