import random

class Seeker:

    """The person looking for the Hider. 

    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __init__(self):
        
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = random.randint(1, 1000)
        
    
    def move_location(self, location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = location
    
    def found_hider(self):
        """Whether or not the seeker has found the hider.

        Args:
            self (seeker): An instance of seeker.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0)
        