# Use a while-true loop to both move and attack.
while True:
    self.moveRight()
    self.moveUp()
    enemy = self.findNearestEnemy()
    self.attack(enemy)
    self.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()
    
    pass