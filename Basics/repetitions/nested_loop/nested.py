print("How many rows should it has?")
rows = int(input())
print("How many columns should it has?")
columns = int(input())
emoji=":-)"
print()
print("Here we go!")
for count in range(0,rows,1):
  for nrows in range(0,columns,1):
    print(emoji, end="")
  print()
# the character of columns are printed in the same line using end=""
# and then the columns is repeated in other line as rows