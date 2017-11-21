listA = [2,5,8,6,8,7,54,65,9,98,45,98,65,78,12,102,154]
listB = []
listC = []
num = input("Enter Number__")

for a in listA:
	if num > a:
		listB.append(a)
		listB.sort()
	else:
		listC.append(a)
		listC.sort()
print "Less to Your number==",listB
print "Greater or Equal to Your number==",listC
