
data = {}

def main():
  entry = int(input("Insert a number"))
  for i in range(1,entry+1):
    data[i]= i*4
  print(data)

main()
