while True:		
	try:
		values = raw_input("Enter The Values: Row,Column__")
		dimensions=[int(x) for x in values.split(',')]
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
