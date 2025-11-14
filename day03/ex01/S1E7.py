from S1E9 import Character

class Baratheon(Character):
    """
    Représente la famille Baratheon.
    """

    family_name = "Baratheon"

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"{self.first_name} | Yeux: {self.eyes}, Cheveux: {self.hairs}, Vivant: {self.is_alive}"

    def __repr__(self):
        return f"Baratheon(first_name='{self.first_name}', is_alive={self.is_alive}, eyes='{self.eyes}', hairs='{self.hairs}')"


class Lannister(Character):
    """
    Représente la famille Lannister.
    """

    family_name = "Lannister"

    def __init__(self, first_name, is_alive=True, eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"{self.first_name} | Yeux: {self.eyes}, Cheveux: {self.hairs}, Vivant: {self.is_alive}"

    def __repr__(self):
        return f"Lannister(first_name='{self.first_name}', is_alive={self.is_alive}, eyes='{self.eyes}', hairs='{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Méthode de classe pour créer un Lannister.
        """
        return cls(first_name, is_alive)