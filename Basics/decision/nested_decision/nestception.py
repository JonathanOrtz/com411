# Display the question
print("Where should I look?")
answer = input()
if (answer=="in the bedrrom"):
  print("Where in the bedroom should I look?")
  bed_answer = input()
  if (bed_answer=="under the bed"):
    print("Found some shoes but no the battery")
  else:
    print("Found some mess but not the battery")
elif(answer=="in the bathroom"):
  print("Where in the bathroom should I look?")
  bath_answer = input()
  if(bath_answer=="in the bathtub"):
    print("Found a rubber duck but no the battery")
  else:
    print("Found a wet surface")
elif(answer=="in the lab"):
  print("where in the lab should I look?")
  lab_answer = input()
  if (lab_answer=="on the table"):
    print("Yes!, I found my battery")
  else:
    print("Found some tools but no the battery")
else:
  print("I do not know where that is but I will keep looking.")