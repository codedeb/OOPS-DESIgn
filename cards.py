import random
class Card():
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for card in ['Spades', 'Hearts', 'Diamond', 'Club']:
            for value in range(1,14):
                self.cards.append(Card(card, value))

    def show(self):
        for val in self.cards:
            val.show()

    def shuffle(self):
        for num in range(len(self.cards)-1,0,-1):
            rand = random.randint(0,num)
            self.cards[num], self.cards[rand] = self.cards[rand], self.cards[num]


    def drawcard(self):
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawcard())

    def showhand(self):
        for card in self.hand:
            card.show()

deck = Deck()
# deck.show()
deck.shuffle()
# # deck.show()
# card = deck.draw()
# card.show()

player = Player('xyz')
player.draw(deck)
player.showhand()