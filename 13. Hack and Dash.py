# You can write code before a loop.
hero.moveRight()
# Break open the "Chest" before using the loop to escape the maze!
hero.moveUp()
hero.attack("Chest")
hero.moveDown()

# Return back back into the main hallway.
ready = hero.isReady("cleave")
while True:
    hero.moveRight(3)
    hero.moveDown(3)


    
    
    # Move 3 times more.
    
