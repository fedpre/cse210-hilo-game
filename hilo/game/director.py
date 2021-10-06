from game.turner import Turner



class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to keep track of the score and control the
    sequence of play.
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        points
        score (number): The total number of points earned.
        turner (Turner): An instance of the class of objects known as Turner."""
    
    def __init__(self):
        """The class constructor.
        Args:
            self (Director): an instance of Director."""
        self.keep_playing = True
        self.score = 300
        self.turner = Turner()


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director."""
        
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means turning the card.
        Args:
            self (Director): An instance of Director."""
        pass

    # Python program to print
    # colored text and background
    

    def do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means the card is turned and the score changes. 
        (see color)
        Args:
            self (Director): An instance of Director."""

        print(f"\nThe card is: {self.turner.first_card}")
        guess = input('Make your guess. Will the next card be higher or lower? [h/l] ')
        points = self.turner.get_points(guess.lower())
        self.score += points
        print(f"The next card was: {self.turner.second_card}")

        if points >= 100:
            print("\x1b[32mCongratulations! You guessed correctly and earned 100 points\x1b[0m")
        else:
            print("\x1b[31mOh no! Your guess is incorrect and you lose 75 points.\x1b[0m")
        print(f"Your running score is: {self.score}")

        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            if choice.lower() == "y":
                self.keep_playing = (choice == "y")
            else:
                print()
                print(f"Thank you for playing! Your final score is: {self.score}")
                self.keep_playing = False
        else:
            print(f"Thank you for playing! Your final score is: {self.score}")
            self.keep_playing = False

















