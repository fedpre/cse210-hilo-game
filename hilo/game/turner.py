import random

# TODO: Define the Thrower class here.

class Turner:
    """ The turner is the player of the game. The turner must turn the card to play.

        Attributes:
            first_card (number): Random number between 1 and 13
            second_card (number): Random number between 1 and 13
            points (num): Value of the points calculated on each turn
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Turner): an instance of Turner

        """
        self.first_card = random.randint(1, 13)
        self.second_card = 0
        self.points = 0


    def get_points(self, guess):
        """The get_points method calculates and returns the total points for the current 
        guess. If the person guesses correctly, it will receive 100 points. If it 
        guesses incorrectly, it will lose 75 points.
        
        Args: 
            self (Turner): an instance of Turner
            guess (string): the user's guess [h/l]
        """
        second_card = self.turn_card()


        if (second_card > self.first_card and guess == 'h') or (second_card < self.first_card and guess == 'l'):
            self.points = 100
        else:
            self.points = -75

        if second_card > self.first_card and guess == 'h':
            self.points = 100
        elif second_card < self.first_card and guess == 'h':
            self.points = -75
        elif second_card > self.first_card and guess == 'l':
            self.points = -75
        elif second_card < self.first_card and guess == 'l':
            self.points = 100
        else:
            self.points = 0

        
        self.first_card = self.second_card
        return self.points


    def turn_card(self):
        """The turn_card method randomly generates a new card for the game.
        
        Args: 
            self (Turner): an instance of Turner
        """
        
        self.second_card = random.randint(1, 13)
        while self.second_card == self.first_card:
            self.second_card = random.randint(1, 13)

        return self.second_card

        
