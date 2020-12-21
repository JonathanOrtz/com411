class Robot:
  # A class attribute
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100
  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY

  def grow(self):
    

  # Instance method repr(to return an formal string representation of the object)
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'
  # Instance method str(to return an informal sring of the object)
  def __str__(self):
    return f'My name is {self.name}'
  
  
  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()
  print(robot)
  print(repr(robot))

