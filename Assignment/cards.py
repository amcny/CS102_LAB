import random

def create():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for value in values:
            card = f"{value} of {suit}"
            deck.append(card)
    return deck

def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

def deal(deck):
    player1_hand = [deck.pop() for _ in range(3)]
    player2_hand = [deck.pop() for _ in range(3)]
    return player1_hand, player2_hand

def compare(card1, card2):
    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    value1 = values_dict[card1.split()[0]]
    value2 = values_dict[card2.split()[0]]
    return value1 - value2

def play():
    deck = create()
    shuffle(deck)
    p1, p2 = deal(deck)
    print("Player 1's hand:", p1)
    print("Player 2's hand:", p2)
    for i in range(3):
        result = compare(p1[i], p2[i])
        if result > 0:
            print("Player 1 wins!")
            return
        elif result < 0:
            print("Player 2 wins!")
            return
    print("It's a draw!")

play()
