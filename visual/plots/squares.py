import matplotlib.pyplot as plt 
# first function
def small ():
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')
# plot for the lines 
# r:o  red with dotted lines and circle in the points
small()
# second function
def medium():
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]
  plt.plot(x, y, 'g--s')
# g--s, green for the color, -- dashes for line and squre on the        points
medium()
# third function
def large():
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]
  plt.plot(x, y, 'b-p')
# b-p, blue as the color, - solid dash for the line and pentagone in    the points
large()
# def run
def run():

  small()
  medium()
  large()
  plt.show()
# after call pf functions we use plt.show() to display the figure
run()