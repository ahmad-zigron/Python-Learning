#Question:
#Python has many built-in functions, and if you do not know how to use it, you can read #document online or find some books. But Python has a built-in document function for every built-in functions.
#   Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#    And add document for your own function
print ("Finds The Documentation of Built-In Functions")
print ("1 For abs()")  
print ("2 for int()")  
print ("3 for raw_input()")
print ("4 for str()")
print ("5 for staticmethod()")
print ("6 for all()")
print ("7 for file()")
print ("8 for bool()")

while True:
	try:
		number = int (input("Enter Related Number__"))
		if(number == 1):
			print(abs.__doc__)
		elif(number == 2):
			print(int.__doc__)
		elif(number == 3):
			print(raw_input.__doc__)
		elif(number == 4):
			print(str.__doc__)

		elif(number == 5):
			print(staticmethod.__doc__)

		elif(number == 6):
			print(all.__doc__)

		elif(number == 7):
			print(file.__doc__)
		elif(number == 8):
			print(bool.__doc__)

		else:
			print("Please Put the Related Number")
		
	except:
		print"Why are you Kiddng me :("
		break


	
