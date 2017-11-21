
number = int(input())

factorial = 1


if number < 0:
   print("Cant Take Factorial for Negative Number")
elif number == 0:
   print("1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print(factorial)
