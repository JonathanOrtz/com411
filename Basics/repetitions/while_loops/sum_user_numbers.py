# ask for the numbers
print("How many numbers should I sum up?")
#declare the input variable
numbertosume=int(input())
#declare the variable of numbers summed
summed=1
#declare the total sum of the numbers
total=0
while(summed<numbertosume):
  print("Please enter", summed, "of", numbertosume)
  number=int(input())
  total=number+summed
  summed=summed+1
#introduce the total
print("The answer is", total)