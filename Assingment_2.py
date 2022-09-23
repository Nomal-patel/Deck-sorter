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


    # Insertion sort in Python

    def mergeSort(self):
        if len(deck.cards) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(self.cards) // 2
            L = self.cards[:r]
            M = self.cards[r:]

            # Sort the two halves

            L.sort()
            M.sort()

            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    self.cards[k] = L[i]
                    i += 1
                else:
                    self.cards[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                self.cards[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                self.cards[k] = M[j]
                j += 1
                k += 1

    def partition(self, low, high):

        # choose the rightmost element as pivot
        pivot = deck.cards[high].rank

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):

            if deck.cards[j].rank <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (deck.cards[i], deck.cards[j]) = (deck.cards[j], deck.cards[i])

        # swap the pivot element with the greater element specified by i
        (deck.cards[i + 1], deck.cards[high]) = (deck.cards[high], deck.cards[i + 1])

        # return the position from where partition is done
        return i + 1

    # function to perform quicksort
    def quickSort(self, low, high):
        if low < high:
            # find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition( low, high)

            # recursive call on the left of pivot
            self.quickSort( low, pi - 1)

            # recursive call on the right of pivot
            self.quickSort( pi + 1, high)





deck=Deck()


deck.shuffle()
print("so what is the " + "\n")


print(deck)

size = 52


deck.quickSort(0, size - 1)
print("Sorted by value: " + "\n")
print(deck)



deck.shuffle()
print("Sorted by suit and value " + "\n")


deck.mergeSort()
print(deck)











