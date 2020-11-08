print("Program started")
ascii_code=abs(int(input("Please enter an ASCII code:")))

for ride in range(32,127,1):
  if ascii_code==ride:
    chr(ascii_code)
    print(f"The character represented by the ASCII code {ascii_code} is {chr(ride)}.")

print("Porgram ended!")