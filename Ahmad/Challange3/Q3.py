#Question 3: 
#Write a program that accepts a sentence and calculate the number of upper case #letters and lower case letters. Suppose the following input is supplied to the program: 
#Hello world! 
#Then, the output should be: 
#UPPER CASE 1 LOWER CASE 9

sample = raw_input("Write any String_:")
lower = 0
upper = 0
other = 0
for i in sample:
	if i.islower():
		lower +=1	
	elif i.isupper():
		upper +=1
	else:
		other +=1
print"Lower Case Letters are_:",lower
print"Upper Case Letters are_:",upper
print"Other Symbols n Signs are_:",other
