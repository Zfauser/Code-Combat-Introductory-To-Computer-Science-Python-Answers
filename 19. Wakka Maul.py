# Welcome to Wakka Maul! Prepare for combat!
# Venture through the maze and pick up gems to fund your warchest.
# Break down doors to unleash allies (or enemies).
# For example, to attack the door labeled "g" use:
#hero.attack("g")
# If you have enough gold, you can call out for help by saying the type of unit you would like to summon!
#hero.say("soldier") to summon a Soldier at the cost of 20 gold!
#hero.say("archer") to summon an Archer at the cost of 25 gold!
while True:
    hero.moveDown()
    hero.moveRight()
    hero.attack("g")
    hero.say("soldier")
