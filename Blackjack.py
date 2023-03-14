# Gra karciana Black Jack (w wersji uproszczonej) z krupierem w postaci komputera

import random

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "A", "A", "A", "A"]
croupier = 0
player = 0
print("Start!")
choice = "Hit"

def primary_loop(croupier, player, choice):
    if croupier < 17:
        print("\nCroupier's move:", "\nCroupier's choose: Hit")
        croupier += Hit()
        if croupier > 21:
            return print("\n--- You won! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
        if croupier == 21:
            return print("\n--- You lost! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
    if choice == "Hit":
        print("Your move!")
        choice = input("Choose Hit or Stand:")
        print("Your choose:", choice)
        if choice == "Hit":
            player += Hit()
            if player > 21:
                return print("\n--- You lost! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
            if player == 21:
                return print("\n--- You won! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
    if choice == "Stand":
        print("\nValue of your cards: ", player)
        if choice == "Stand" and croupier >= 17:
            if player > croupier:
                return print("\n--- You won! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
            if player < croupier:
                return print("\n--- You lost! ---", "\nValue of croupier's cards:", croupier, "   Value of your cards:", player)
            if player == croupier:
                return print("\n--- Draw! ---")
    print("Value of croupier's cards:", croupier, "   Value of your cards:", player)
    primary_loop(croupier, player, choice)

def Hit():
    card = random.choice(cards)
    cards.remove(card)
    print("The card is:", card, "\n")
    if card == "A":
        return 11
    else:
        return card

primary_loop(croupier, player, choice)
