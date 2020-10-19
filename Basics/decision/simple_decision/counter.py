#asking for the first number
print("Please introduce the first whole number")
first = int(input())
#asking for the second number
print("Please introduce the second whole number")
second = int(input())
#asking for the third number
print("Please introduce the third whole number")
third = int(input())
oddnumber=0
evennumber=0
if (first%2==0):
  evennumber=evennumber+1
else:
  oddnumber=oddnumber+1
if(second%2==0):
  evennumber=evennumber+1
else:
  oddnumber=oddnumber+1
if(third%2==0):
  evennumber=evennumber+1
else:
  oddnumber=oddnumber+1

print("there were {} odd number and there were {} even numbers".format(oddnumber, evennumber))