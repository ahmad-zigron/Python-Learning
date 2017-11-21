#Question 4:
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

name = "Ahmad"
company = "Zigron"
age = 23
cgpa = 3.12

print "%s is a DevOps Intern in %s" % (name,company) 
print "%s is %d old" %(name,age) 
print "His cgpa is %f" % (cgpa)
print "His cgpa is %.2f" % (cgpa)
print "His cgpa is %+.2f" % (cgpa)
while True:
	try:
		a = raw_input("Enter the Value of a__")
		n1 = int( "%s" % a )
		n2 = int("%s%s" % (a,a))
		n3 = int("%s%s%s" % (a,a,a))
		n4 = int("%s%s%s%s" % (a,a,a,a))
		print "The Value of a+aa+aaa+aaaa ==", n1+n2+n3+n4
		break
	except:
		print" Kindly Use Integer Values"
		continue


