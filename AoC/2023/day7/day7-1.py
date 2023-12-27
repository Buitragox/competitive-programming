"""
Jhoan Buitrago
27/12/2023 dd/mm/yyyy

https://adventofcode.com/2023/day/7

1. To solve this problem first determine the hand type of each given hand.
2. Then give numeric value to each hand based on the value and order of the cards.
3. Finally sort the list from weakest to strongest hand type. If there are two hands
   with the same type, compare them with the hand value from least to most.

Hand value:
    To give a numeric value convert the hand to a base 13 number and then cast it to int.
    Why base 13? Because there are 13 possible cards and they can be sorted from best to worst, so we give them
    a numeric value.
"""

from sys import stdin
from enum import IntEnum

card_to_int = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, 
                   '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

card_to_base13 = {'A': 'c', 'K': 'b', 'Q': 'a', 'J': '9', 'T': '8', '9': '7', 
               '8': '6', '7': '5', '6': '4', '5': '3', '4': '2', '3': '1', '2': '0'}

    
class HandTypes(IntEnum):
    Nothing = 0
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeKind = 4
    FullHouse = 5
    FourKind = 6
    FiveKind = 7


class Hand:
    def __init__(self, cards: str, bid: str) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.hand_type = HandTypes.Nothing
        self.find_hand_type()
        self.cards_doz = "".join([card_to_base13[c] for c in cards])
        self.hand_value = int(self.cards_doz, base=13)
        
        
    def __lt__(self, other) -> bool:
        """
        Define the < operator to use the sort function.
        """
        if self.hand_type == other.hand_type:
            return self.hand_value <= other.hand_value
        else:
            return self.hand_type < other.hand_type
    

    def __str__(self) -> str:
        return f"{self.cards} {self.bid}"
        
    def find_hand_type(self):
        """
        Determine the hand type by first counting the cards. 
        Then determine if there is a Three|Four|Five of a kind
        and how many pairs there are.
        If there are no Four or Five of a kind, look for the next 
        best type.
        """
        card_count = [0 for _ in range(13)]
        for c in self.cards:
            card_int = card_to_int[c]
            card_count[card_int] += 1

        has_triple = False
        pair_count = 0

        for c in card_count:
            if c == 5:
                self.hand_type = HandTypes.FiveKind
                break
            elif c == 4:
                self.hand_type = HandTypes.FourKind
                break
            elif c == 3:
                has_triple = True
            elif c == 2:
                pair_count += 1
        
        if self.hand_type == HandTypes.Nothing:
            if has_triple and pair_count > 0:
                self.hand_type = HandTypes.FullHouse
            elif has_triple:
                self.hand_type = HandTypes.ThreeKind
            elif pair_count == 2:
                self.hand_type = HandTypes.TwoPair
            elif pair_count == 1:
                self.hand_type = HandTypes.OnePair
            else:
                self.hand_type = HandTypes.HighCard
        


def main():
    line = stdin.readline()
    hands: list[Hand] = []

    while line != "":
        cards, bid = line.strip().split(" ")
        hand = Hand(cards, bid)
        hands.append(hand)
        line = stdin.readline()
    hands.sort()
    total = 0
    for i, hand in enumerate(hands, start=1):
        total += hand.bid * i
    
    print(total)


if __name__ == "__main__":
    main()