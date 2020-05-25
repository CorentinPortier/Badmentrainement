class Player:
  def __init__(self, name):
    self.name = name
    self.adversory = []
    self.oppenent = None

  def __str__(self):
    return self.name

  def set_opponent(self, opponent):
    self.adversory.append(opponent)
    self.oppenent = opponent
    opponent.adversory.append(self)

class Gymnase:
  def __init__(self, name, terrains):
    self.name = name
    self.terrains = terrains
    self.size = 0

    for terrain in terrains:
      self.size += terrain.size

class Terrains:
  def __init__(self, type):
    self.type = type
    if self.type == "single":
      self.size = 1
    elif self.type == "double":
      self.size = 2

def find_opponent(player, players):
  for opponent in players:
    if player.name != opponent.name:
      print("As {} played against {} ?".format(player, opponent))
      if opponent not in player.adversory:
        print("No. New opponent is {}".format(opponent))
        return opponent
      else:
        print("Yes")
  return None

def calculate_round(players, gymnase):
  terrains = gymnase.size
  while players:
    if not terrains:
      print("No terrains left")
      standby = players
      break
    player = players.pop()
    print("Player", player)
    if len(players) == 0:
      print("No opponent left. {} will not play this round".format(player))
      standby.append(player)
    opponent = find_opponent(player, players)
    if not opponent:
      break
    player.set_opponent(opponent)
    players.remove(opponent)
    terrains -= 1

  print("Standby players:")
  for player in standby:
    print(player)

jean = Player("Jean")
luc = Player("luc")
marie = Player("Marie")
george = Player("George")
marc = Player("Marc")

terrain1 = Terrains("single")
gymnase = Gymnase("Mymy", [terrain1])

marc.adversory.append(marie)
marc.adversory.append(jean)
marc.adversory.append(george)
print(luc.adversory)

players = [jean, luc, marie, george, marc]

standby = []

terrains = 1

calculate_round(players, gymnase)
