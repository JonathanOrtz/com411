print("Program started")
character=input("Please enter a standar character: ")
value=0
if len(character)==1:
  ord(character)
  value=value+ord(character)
  print("The ASCII code for", character, "is", value)
else:
  print("ERROR!")

print("Program ended!")

