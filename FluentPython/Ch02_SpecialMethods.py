import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[-1])
print(deck[0])
print(deck[1])

from random import choice

print(choice(deck))
print(choice(deck))
print(choice(deck))

# First 3 cards
print(deck[:3])

# Pick only Aces, start with 12th and skip 13 cards to select only Aces
print(deck[12::13])


# Implementing __getitem__ special method, make the Deck Iterable
for card in deck:
    print(card)

# "in" works because its iterable
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beast') in deck)


# Sorting: Aces -> Spades -> Hearts -> Diamonds -> Clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(rank_value, len(suit_values) , suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

# By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like a standard Python sequence, 
# allowing it to benefit from core language features (e.g., iteration and slicing) and from the standard library

