def sum_weights(weight_beep, weight_bop):
  total_weight=weight_beep+weight_bop
  return total_weight

def calc_avg_weight(weight_beep, weight_bop):
  average_weight= (weight_beep+weight_bop)/2
  return average_weight

def run():
  weight_beep=int(input("\nWhat is the weight of Beep? "))
  weight_bop=int(input("\nWhat is the weight of bop? "))
  choose=input("\nWhat would you like to calculate (sum or average)? ")
  if choose=="sum":
    print(sum_weights(weight_beep, weight_bop))
  elif choose=="average":
    print(calc_avg_weight(weight_beep, weight_bop))

run()
