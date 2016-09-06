class Pokemon(object):
  def __init__(self, name, cp):
    self.name = name
    self.cp = cp
  
  def type(self):
    return 'Unknown'
  
  def weakList(self):
    return []
  
  def strongList(self):
    return []
  
  def efficiency(self, pokemon):
    if pokemon.type() in self.weakList():
      return 0.8;
    if pokemon.type() in self.strongList():
      return 1.25;
    return 1;
  
  def defeat(self, pokemon):
    return self.cp * self.efficiency(pokemon) > pokemon.cp
    
  def info(self):
    print 'My name is %s, CP is %d, type is %s.' % (self.name, self.cp, self.type())
  
class Grass(Pokemon):
  def __init__(self, name, cp):
    Pokemon.__init__(self, name, cp)
    
  def type(self):
    return 'Grass'
  
  def weakList(self):
    return ['Fire', 'Bug', 'Poison', 'Flying']
  
  def strongList(self):
    return ['Water', 'Ground', 'Rock']

class Fire(Pokemon):
  def __init__(self, name, cp):
    Pokemon.__init__(self, name, cp)
  
  def type(self):
    return 'Fire'
  
  def weakList(self):
    return ['Ground', 'Rock', 'Water']
  
  def strongList(self):
    return ['Grass', 'Bug']
  
class Water(Pokemon):
  def __init__(self, name, cp):
    Pokemon.__init__(self, name, cp)
    
  def type(self):
    return 'Water'
  
  def weakList(self):
    return ['Grass', 'Electric']
  
  def strongList(self):
    return ['Fire', 'Ground', 'Rock']
  
class Electric(Pokemon):
  def __init__(self, name, cp):
    Pokemon.__init__(self, name, cp)
    
  def type(self):
    return 'Electric'
  
  def weakList(self):
    return ['Grass', 'Ground']
  
  def strongList(self):
    return ['Flying', 'Water']
  
class Exeggutor(Grass):
  def __init__(self, name, cp):
    Grass.__init__(self, name, cp)

class Arcanine(Fire):
  def __init__(self, name, cp):
    Fire.__init__(self, name, cp)

# Main entrance

if __name__ == '__main__':
    pass
  
exeggutor = Exeggutor('Power', 2000)
exeggutor.info()

exeggutor2 = Exeggutor("Weak", 1203)
exeggutor2.info()

arcanine = Arcanine('Ground', 1800)
print arcanine.defeat(exeggutor)


