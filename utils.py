import random


class CardsDeck:
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []

    @classmethod
    def populate_deck(cls):
        for card in cls.cards:
            for _ in range(4):
                cls.deck.append(card)

    @classmethod
    def shuffled(cls):
        random.shuffle(cls.deck)

    @classmethod
    def split_deck(cls):
        return [cls.deck[:26], cls.deck[26:]]


class Player:
    def __init__(self, name):
        self.name = name
        self.stack = []

    def get_card(self, num):
        self.stack = self.stack[num:]
        return self.stack[0:num]

    def add_cards(self, cards_1, cards_2):
        self.stack = self.stack + cards_1 + cards_2

    def is_winner():
        ...


class Game:
    ...


def get_players_names():
    name1 = input("Player 1 name: ")
    name2 = input("Player 2 name: ")
    return [name1, name2]


def print_table():
    ...


# cards_deck = CardsDeck()
# cards_deck.populate_deck()
# cards_deck.shuffled()
# print(cards_deck.deck)
# print(cards_deck.split_deck())
