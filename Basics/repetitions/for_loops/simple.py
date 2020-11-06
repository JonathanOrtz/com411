#display the message 
print("How many mountains should I display?")
mountains=int(input())
#asking for the number of mountains
for count in range(mountains):
  print("     ---      ")
  print("    /   \__ ")
  print("   /  ^    \ ")
  print("  /   ^   ^ \ ")
  print(" /___________\  ")


# another way to do
#display the message 
print("How many mountains should I display?")
mountains=int(input())
#asking for the number of mountains
for count in range(0,mountains,1):
  print("     ---      ")
  print("    /   \__ ")
  print("   /  ^    \ ")
  print("  /   ^   ^ \ ")
  print(" /___________\  ")
