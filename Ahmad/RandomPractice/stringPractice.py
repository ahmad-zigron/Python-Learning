name = "Ahmad"
company = "Zigron"
age = 23
cgpa = 3.12

print "%s is a DevOps Intern in %s" % (name,company) 
print "%s is %d old" %(name,age) 
print "His cgpa is %f" % (cgpa)
print "His cgpa is %.2f" % (cgpa)
print "His cgpa is %+.2f" % (cgpa)
a = raw_input()
n1 = int( "%s" % a )
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
n4 = int("%s%s%s%s" % (a,a,a,a))
print n1+n2+n3+n4
