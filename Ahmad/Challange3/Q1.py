#Question 1: 
#Write a program, which will find all such numbers between 1000 and 3000 
#(both included) such that each digit of the number is  an even number. The numbers obtained #should be printed in a comma-separated sequence on a single line.

print("Even numbers between 1000 to 3000")
while True:
 	try:		
		a = 1000
		b = 3000
		values = []
		for i in range(a, b+1):
			if (i%2==0): 
			    values.append(str(i))
		print (",".join(values))
		break
	except:
		print"Please Enter Exact Integers range "
		continue
