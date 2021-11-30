SPADES = "\u2660"
HEARTS = "\u2665"
DIAMONDS = "\u2666"
CLUBS = "\u2663"

class Card:
    
    def __init__(self, suit: str, value: str):
        
        self.suit = suit
        self.value = value
    
    def __str__(self):
        
        return "\u250C"+"\u2500"*7+"\u2510"+"\n"+
               "

print("\u250C", "\u2500"*7, "\u2510", sep="")
print("\u2502", "A      ", "\u2502", sep="")
print("\u2502", "       ", "\u2502", sep="")
print("\u2502", f"   {SPADES}   ", "\u2502", sep="")
print("\u2502", "       ", "\u2502", sep="")
print("\u2502", "      A", "\u2502", sep="")
print("\u2514", "\u2500"*7, "\u2518", sep="")

print(SPADES, HEARTS, DIAMONDS, CLUBS)