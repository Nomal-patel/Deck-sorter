import random


class Card:
    """Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank -1] ,
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        """Checks whether self and other have the same rank and suit.
        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.
        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
print("so how is theshvgdc " + str(Card())+" plus sum more")


class Deck:
    """Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.ranking = []
        for suit in range(4):
            for rank in range(1, 14):
                ranks = Card(rank)
                self.ranking.append(ranks)

    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)






    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

    # Bubble sort in Python

    def bubbleSort(self):
        # We want to stop passing through the list
        # as soon as we pass through without swapping any elements
        has_swapped = True

        while (has_swapped):
            has_swapped = False
            for i in range(len(deck.cards) - 1):
                if deck.cards[i].rank > deck.cards[i + 1].rank:
                    # Swap
                    deck.cards[i].rank, deck.cards[i+1].rank = deck.cards[i+1].rank, deck.cards[i].rank
                    has_swapped = True



    # Insertion sort in Python

    def insertionSort(self):

        for step in range(1, len(self.cards)):
            key = self.cards[step]
            j = step - 1

            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].
            while j >= 0 and key < self.cards[j]:
                self.cards[j + 1] = self.cards[j]
                j = j - 1

            # Place key at after the element just smaller than it.
            self.cards[j + 1] = key



deck=Deck()
deck.shuffle()
print("so what is the " + "\n")
print("so what is the " + "\n")
print("so what is the " + "\n")

print(deck)

deck.bubbleSort()
print("so what is the " + "\n")
print(deck)

"""
deck.shuffle()
print(deck)

deck.insertionSort()
print("so what is the " + "\n")
print("so what is the " + "\n")

print(deck)

"""










""""
for i in range(len(deck) - 1, 0, -1):
    j = random.randint(0, i)

    deck[i], deck[j] = deck[j], deck[i]

for i in range(len(deck)):
    print("this is " + deck[i])
"""