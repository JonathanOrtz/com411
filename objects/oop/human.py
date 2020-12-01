class Human:
  #class attribute
  MAX_ENERGY  = 100
  # initializer(special instance method)
  def __init__(self):
    # instance attributes
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY
  #  An instance method (to display)
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.display()