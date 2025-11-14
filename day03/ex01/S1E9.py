from abc import ABC, abstractmethod

class Character(ABC):
    """
    Classe abstraite représentant un personnage.
    first_name : prénom du personnage
    is_alive : état de vie (vivant ou mort)
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructeur d'un personnage.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Change l'état du personnage à 'mort'.
        """
        self.is_alive = False


class Stark(Character):
    """
    Classe représentant un membre de la famille Stark.
    Hérite de Character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructeur d'un Stark.
        """
        super().__init__(first_name, is_alive)
