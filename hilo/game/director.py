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
        self.guess = ""


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director."""
        
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
            
    #this will check the entered options and reject not allowed
    def check_option(opt1, opt2, question):
      choice = "x"
      while choice != opt1 and choice != opt2:
          choice = input(f"{question} [{opt1}/{opt2}] ").lower()
          if choice != opt1 and choice != opt2:
              print(f"{choice} is not allowed, try again...")
      return choice
    
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means asking for the guess to the user.
        Args:
            self (Director): An instance of Director."""

        print(f"\nThe card is: {self.turner.first_card}")

        self.guess = check_option("h", "l", "Make your guess. Will the next card be higher or lower?")        

      # Python program to print
      # colored text and background    

        self.guess = input('Make your guess. Will the next card be higher or lower? [h/l] ')

      # Python program to print
      # colored text and background
    


    def do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means the card is turned and the score changes. 
        (see color)
        Args:
            self (Director): An instance of Director."""
        points = self.turner.get_points(self.guess.lower())
        self.score += points
        print(f"The next card was: {self.turner.second_card}")

        if points >= 100:
            print("\x1b[32mCongratulations! You guessed correctly and earned 100 points\x1b[0m")

        else:
            print("\x1b[31mOh no! Your guess is incorrect and you lose 75 points.\x1b[0m")
        print(f"Your running score is: {self.score}")

        else:
            print("\x1b[31mOh no! Your guess is incorrect and you lose 75 points.\x1b[0m")
        print(f"Your running score is: {self.score}")

        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            if choice.lower() == "y":
                self.keep_playing = (choice == "y")
            else:
                print()
                print(f"Thank you for playing! Your final score is: {self.score} points")
                self.keep_playing = False
        else:
            print(f"Thank you for playing! Your final score is: {self.score} points")
            self.keep_playing = False


        if self.score > 0:
            choice = check_option("y", "n", "Keep playing?")
            if choice == "y":
                self.keep_playing = True

        if self.score < 0 or choice == "n":
            print(f"\nThank you for playing! Your final score is: {self.score} points")
            self.keep_playing = False















