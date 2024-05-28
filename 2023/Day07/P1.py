from pandas import DataFrame
import pandas as pd
from pandas.api.types import CategoricalDtype
from typing import List


list_values = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind']
list_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def read_input(file_path: str) -> DataFrame: 
    '''Read input and return as DataFrame'''
    with open(file_path, 'r') as file:
        lines = file.readlines()
    hands: List[str] = []
    bids: List[int] = []
    types: List[str] = []
    ranks: List[int] = []

    for i, line in enumerate(lines):
        hands.append(line.split()[0])
        bids.append(int(line.split()[1]))
        types.append(get_type(line.split()[0]))
        ranks.append(i + 1)

    df = pd.DataFrame({'hands': hands, 'bids': bids, 'types': types, 'ranks': ranks})

    type_order = CategoricalDtype(categories=list_values, ordered=True)

    df['types'] = df['types'].astype(type_order)

    df = df.sort_values(by=['types', 'bids'], ascending=[True, True])

    # Add a column with hand values converted to a list of numbers for sorting
    df['hand_values'] = df['hands'].apply(convert_hand_to_value)

    df = df.sort_values(by=['types', 'hand_values'], ascending=[True, True])

    df = df.drop(columns=['hand_values'])

    return df


def get_type(hand: str) -> str:
    '''Get the type of a hand'''
    occurence: List[int] = []
    for card in hand:
        occurence.append(hand.count(card))
    if max(occurence) == 5:
        return list_values[6]
    elif max(occurence) == 4:
        return list_values[5]
    elif max(occurence) == 3:
        if min(occurence) == 2:
            return list_values[4]
        else:
            return list_values[3]
    elif max(occurence) == 2:
        if occurence.count(2) == 2:
            return list_values[2]
        else:
            return list_values[1]
    else:
        return list_values[0]


def convert_hand_to_value(hand: str) -> List[int]:
    '''Convert hand to value'''
    return [list_cards.index(card) for card in hand]


def main():
    print("Hello World!")
    df = read_input('inputP1.txt')
    print(df)


if __name__ == "__main__":
    main() 
