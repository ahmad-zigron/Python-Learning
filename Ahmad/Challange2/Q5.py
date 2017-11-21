#Question:
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

while True:		
	try:
		values = raw_input("Enter The Values: Row,Column__")
		dimensions=[int(a) for a in values.split(',')]
		rowNum=dimensions[0]
		colNum=dimensions[1]
		multilist = [[0 for col in range(colNum)] for row in range(rowNum)]	
		for row in range(rowNum):
		   	for col in range(colNum):
				multilist[row][col]= row*col
		print multilist 
		break
	except:
		print"Please Re-Enter The Value of Row And Columns"
		continue
