#Question 2:
#Write a program that accepts a sentence and calculate the number of letters and digits. #Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

sample = raw_input("Write a String__:")
letters = 0
numeric = 0
space = 0
other = 0
for i in sample:
	if i.isdigit():
		numeric +=1
	elif i.isalpha():
		letters +=1
	elif i.isspace():
		space+=1
	else:
		other+=1
print "Letters in This String Are_:", letters
print "Digits in This String Are_:",numeric
print "Spaces in This String Are_:",space
print "Other Signs in This String Are_:",other
