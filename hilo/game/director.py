from game.turner import Turner

class Director:
    # A code template for a person who directs the game. The responsibility of
    # this class of objects is to keep track of the score and control the
    # sequence of play.
    # Attributes:
    #     keep_playing (boolean): Whether or not the player wants to keep playing.
    #     score (number): The total number of points earned.
    #     turner (Turner): An instance of the class of objects known as Turner.
    
    def __init__(self):
        # The class constructor.
        # Args:
        #     self (Director): an instance of Director.
        self.keep_playing = True
        self.score = 300
        self.turner = Turner()

    def start_game(self):
        # Starts the game loop to control the sequence of play.
        # Args:
        #     self (Director): an instance of Director.
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        # Gets the inputs at the beginning of each round of play. In this case,
        # that means throwing the dice.
        # Args:
        #     self (Director): An instance of Director.
        self.turner
        self.turner.turner_card()

    def do_updates(self):
        # Updates the important game information for each round of play. In
        # this case, that means updating the score.
        # Args:
        #     self (Director): An instance of Director.
        points = self.turner.get_points()
        self.score += points
        if points <= 0:
            print()
            print()
            print("Better luck next time!")
            self.score = 0

    def do_outputs(self):
        # Outputs the important game information for each round of play. In
        # this case, that means the dice that were rolled and the score.
        # Args:
        #     self (Director): An instance of Director.

        print(f"\nYou card is: {self.turner.card}")
        print(f"Your score is: {self.score}")

        if self.turner.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
            print("Better luck next time!")

















