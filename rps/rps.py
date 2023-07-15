class Game:
  def __init__(self):
    self.p1 = ""
    self.p2 = ""


  def play_hand(self, player, option): 
    if player == "p1":
      self.p1 = option
    elif player == "p2":
      self.p2 = option      
    return f"{player} has played {option}"

  def result(self):
    if self.p1 == self.p2:
      return "Draw"
    elif (self.p1 == "paper" and self.p2 == "rock"):
      return "p1 wins"
    elif (self.p2 == "paper" and self.p1 == "rock"):
      return "p2 wins"