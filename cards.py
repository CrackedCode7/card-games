import colors
import random

SPADES = "\u2660"
HEARTS = "\u2665"
DIAMONDS = "\u2666"
CLUBS = "\u2663"

class Card:
    
    def __init__(self, value:str, suit: str):
        
        self.face_up = False
        self.value = value
        
        if suit.upper() == "SPADES":
            self.suit = SPADES
            self.color = colors.RESET
        elif suit.upper() == "HEARTS":
            self.suit = HEARTS
            self.color = colors.RED
        elif suit.upper() == "DIAMONDS":
            self.suit = DIAMONDS
            self.color = colors.RED
        elif suit.upper() == "CLUBS":
            self.suit = CLUBS
            self.color = colors.RESET
        else:
            self.suit = " "
            self.color = colors.RESET

    
    def __str__(self):
        if len(self.value) == 1:
            return colors.RESET+self.color+\
                   "\u250C"+"\u2500"*5+"\u2510"+"\n"+\
                   "\u2502"+self.value+" "*4+"\u2502"+"\n"+\
                   "\u2502"+" "*2+self.suit+" "*2+"\u2502"+"\n"+\
                   "\u2502"+" "*4+self.value+"\u2502"+"\n"+\
                   "\u2514"+"\u2500"*5+"\u2518"+\
                   colors.RESET
        else:
            return colors.RESET+self.color+\
                   "\u250C"+"\u2500"*5+"\u2510"+"\n"+\
                   "\u2502"+self.value+" "*3+"\u2502"+"\n"+\
                   "\u2502"+" "*2+self.suit+" "*2+"\u2502"+"\n"+\
                   "\u2502"+" "*3+self.value+"\u2502"+"\n"+\
                   "\u2514"+"\u2500"*5+"\u2518"+\
                   colors.RESET
    
    """def __str__(self):
        if len(self.value) == 1:
            return colors.RESET+self.color+\
                   "\u250C"+"\u2500"*7+"\u2510"+"\n"+\
                   "\u2502"+self.value+" "*6+"\u2502"+"\n"+\
                   "\u2502"+" "*7+"\u2502"+"\n"+\
                   "\u2502"+" "*3+self.suit+" "*3+"\u2502"+"\n"+\
                   "\u2502"+" "*7+"\u2502"+"\n"+\
                   "\u2502"+" "*6+self.value+"\u2502"+"\n"+\
                   "\u2514"+"\u2500"*7+"\u2518"+\
                   colors.RESET
        else:
            return colors.RESET+self.color+\
                   "\u250C"+"\u2500"*7+"\u2510"+"\n"+\
                   "\u2502"+self.value+" "*5+"\u2502"+"\n"+\
                   "\u2502"+" "*7+"\u2502"+"\n"+\
                   "\u2502"+" "*3+self.suit+" "*3+"\u2502"+"\n"+\
                   "\u2502"+" "*7+"\u2502"+"\n"+\
                   "\u2502"+" "*5+self.value+"\u2502"+"\n"+\
                   "\u2514"+"\u2500"*7+"\u2518"+\
                   colors.RESET"""


class Deck:
    
    suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.reset()

    def __str__(self):
        return "".join(["\n"+str(card) for card in self.deck])
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def draw(self):
        card = self.deck[-1]
        self.deck.remove(card)
        return card
    
    def reset(self):
        self.deck = [Card(value, suit) for suit in Deck.suits for value in Deck.values]
