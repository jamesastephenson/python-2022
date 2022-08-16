from random import randint

class Die():
    """a class representing a single die"""

    def __init__(self, numSides=20):
        """set # of sides (D#)"""
        self.numSides = numSides

    def roll(self):
        """return a random value between 1 and numSides"""
        return randint(1, self.numSides)

def RollDice(numDice):
    while numDice > 0:
        print(Die().roll())
        numDice -= 1

RollDice(3)