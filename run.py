from cards import Card, Deck


class GameBoard:
    
    def __init__(self):
        
        self.deck = Deck()
        self.stock = []
        self.waste = []
        self.foundations = []
        self.tableau = {i: [] for i in range(1, 8)}
    
    def deal(self):
    
        for i in range(1, 8):
            for key in self.tableau:
                print(i, key)
                if key >= i:
                    self.tableau[i].append(self.deck.draw())
                    if key == i:
                        self.tableau[i][-1].face_up = True
        
        while len(self.deck.deck) != 0:
            self.stock.append(self.deck.draw())
        
        self.stock.reverse()

    def draw_from_stock(self):
        
        pass


if __name__ == '__main__':
    
    board = GameBoard()
    board.deal()
    for col in board.tableau:
        
        for card in board.tableau[col]:
            print(card.face_up)