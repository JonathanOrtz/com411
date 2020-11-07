print("What strange markings do you see?")
strange_markings=input()
print("Identifying...")
for markings in range(0,len(strange_markings),1):
  print("Index",markings,":",strange_markings[markings])