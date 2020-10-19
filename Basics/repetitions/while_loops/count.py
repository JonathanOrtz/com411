print("How many live cables must I avoid?")
cabletoavoid=int(input())
cableavoided=0
while(cableavoided<cabletoavoid):
  cableavoided=cableavoided+1
  print("Avoiding...Done! {} live cable avoided".format(cableavoided))
print("All cable has been avoided")