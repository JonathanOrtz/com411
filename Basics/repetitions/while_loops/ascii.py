print("How many bars should be charged?")
barstocharge=int(input())
barschanged=0
while(barschanged<barstocharge):
  barschanged=barschanged+1
  print("\nCharging:"," █ "*barschanged)
print("\nThe battery is full charged")