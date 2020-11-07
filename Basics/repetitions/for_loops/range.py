print("What level of brightness is required?")
levelbrightness=int(input())
for brightness in range(2,levelbrightness+1,2):
  print("Beep's brightness level:","*"*brightness)
  print("Bop's brightness level:", "*"*brightness)

print("Adjustments complete!")

