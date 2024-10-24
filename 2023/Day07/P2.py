from pandas import DataFrame
import pandas as pd
from pandas.api.types import CategoricalDtype
from typing import List


list_values = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind']
list_cards = ['', 'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def read_input(file_path: str) -> DataFrame: 
    '''Read input and return as DataFrame'''
    with open(file_path, 'r') as file:
        lines = file.readlines()
    hands: List[str] = []
    bids: List[int] = []
    types: List[str] = []

    for i, line in enumerate(lines):
        hands.append(line.split()[0])
        bids.append(int(line.split()[1]))

    df = pd.DataFrame({'hands': hands, 'bids': bids})
    
    type_order = CategoricalDtype(categories=list_values, ordered=True)
 
    df['new_hand'] = df['hands'].apply(convert_hand)
    df['types'] = df['new_hand'].apply(get_type)
    df['types'] = df['types'].astype(type_order)

    df = df.sort_values(by=['types', 'bids'], ascending=[True, True])

    df['card_one'] = df['hands'].apply(convert_hand_to_value_card_one)
    df['card_two'] = df['hands'].apply(convert_hand_to_value_card_two)
    df['card_three'] = df['hands'].apply(convert_hand_to_value_card_three)
    df['card_four'] = df['hands'].apply(convert_hand_to_value_card_four)
    df['card_five'] = df['hands'].apply(convert_hand_to_value_card_five)

    df = df.sort_values(by=['types', 'card_one', 'card_two', 'card_three', 'card_four', 'card_five'], ascending=[True, True, True, True, True, True])

    # Reset index otherwise rows are not sorted, and index is wrong
    df = df.reset_index(drop=True)

    df['score'] = (df.index + 1) * df['bids']

    return df


def get_highest_occurence_card(hand: str) -> int:
    '''get highest occurence card in hand'''
    max_occurence = 0
    max_card = ''
    for card in hand:
        if ((hand.count(card) > max_occurence)
            or (hand.count(card) == max_occurence 
                and list_cards.index(card) > list_cards.index(max_card))):
            max_occurence = hand.count(card)
            max_card = card
    return list_cards.index(max_card)


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
            return list_values[1]
        else:
            return list_values[2]
    else:
        return list_values[0]


def get_highest_occurence_value_card_other_than_jack(hand: str) -> str:
    '''Get the highest occurence value card other than jack'''
    hand_without_jack = hand.replace('J', '')
    max_occurence = 0
    max_occurence_card = ''
    for card in hand_without_jack:
        if ((hand_without_jack.count(card) > max_occurence) 
            or (hand_without_jack.count(card) == max_occurence 
                and convert_card_to_value(card) > convert_card_to_value(max_occurence_card))):
            max_occurence = hand_without_jack.count(card)
            max_occurence_card = card
    return max_occurence_card


def convert_hand(hand: str) -> str:
    '''Transform J in hand to the best card'''
    if hand.count('J') == 0:
        return hand
    if hand.count('J') == 5:
        return 'AAAAA'
    new_hand = hand.replace('J', get_highest_occurence_value_card_other_than_jack(hand))
    if len(new_hand) != 5:
        print('hand', hand, ', new_hand', new_hand)
        raise TypeError('Error in hand conversion')
    return new_hand


def test_get_type() -> None:
    '''Testing the get type function'''
    assert(get_type('AAAAA') == list_values[6])
    assert(get_type('AAAKA') == list_values[5])
    assert(get_type('KKKQQ') == list_values[4])
    assert(get_type('AAAQK') == list_values[3])
    assert(get_type('AAKKQ') == list_values[2])
    assert(get_type('AAQJK') == list_values[1])
    assert(get_type('ATQJK') == list_values[0])


def convert_hand_to_value(hand: str) -> List[int]:
    '''Convert hand to value'''
    return [convert_card_to_value(card) for card in hand]


def convert_card_to_value(card: str) -> int:
    '''Convert card to value'''
    return list_cards.index(card)


def convert_hand_to_value_card_one(hand: str) -> int:
    return convert_card_to_value(hand[0])


def convert_hand_to_value_card_two(hand: str) -> int:
    return convert_card_to_value(hand[1])


def convert_hand_to_value_card_three(hand: str) -> int:
    return convert_card_to_value(hand[2])


def convert_hand_to_value_card_four(hand: str) -> int:
    return convert_card_to_value(hand[3])


def convert_hand_to_value_card_five(hand: str) -> int:
    return convert_card_to_value(hand[4])


def get_score(df: DataFrame) -> int:
    '''Get the score of the set'''
    return df['score'].sum()


def main():
    test_get_type()
    df_test = read_input('test_input.txt')
    assert(get_score(df_test) == 5905)
    print('Test passed')

    df = read_input('inputP1.txt')
    print(df)
    print(df['score'].sum())


if __name__ == "__main__":
    main() 
