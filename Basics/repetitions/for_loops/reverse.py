print("What phrase do you see?")
phrase=input()
print("reversing...\nThe phrase is:", end="")
for count in range(len(phrase)-1, -1, -1):
  print(phrase[count], end="")

# end="" is used to put all characters in the same line instead of diferent lines for each character
# ask for -1 -1 -1(the starting)