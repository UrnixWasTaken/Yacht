YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    x = set(dice)
    if category == YACHT:
        if len(x) == 1:
            return 50
        else:
            return 0
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        if len(x) == 2 and dice.count(dice[0]) in [3,2]:  
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if len(x) in [2,1] and dice.count(dice[0]) in [4,1,5]:
            return max(x, key=dice.count) * 4
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        dice.sort()
        if dice == [1,2,3,4,5]:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        dice.sort()
        if dice == [2,3,4,5,6]:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)