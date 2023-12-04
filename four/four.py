import re
import pprint as pp


def first(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            cards = file.readlines()
    else:
        cards = test.split("\n")

    res = 0
    for card in cards:
        card = format_card(card)
        wins = check_wins(card)
        if wins:
            res += 2 ** (wins - 1)

    return res


def second(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            cards = file.readlines()
    else:
        cards = test.split("\n")

    rescards = [[f"Card{i+1}", x, 1] for i, x in enumerate(cards)]

    for idx, card in enumerate(rescards):
        card[1] = format_card(card[1])
        wins = check_wins(card[1])
        for i in range(card[2]):
            for j in range(wins):
                rescards[idx + j + 1][2] += 1

    res = sum(card[2] for card in rescards)
    return res


def check_wins(card):
    (mynums, winnums) = card
    matches = re.findall(
        r" " + " | ".join(mynums) + " ", " " + "  ".join(winnums) + " "
    )
    return len(matches)


def format_card(card):
    card = card.split("|")
    mynums = card[0].split(":")[1].split(" ")
    mynums = [x for x in mynums if x.strip()]
    winnums = card[1].split(" ")
    winnums = [x.strip() for x in winnums if x.strip()]
    return (mynums, winnums)


if __name__ == "__main__":
    test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    # res = first("input.txt", test)
    # res = first("input.txt")
    # res = second("input.txt", test)
    res = second("input.txt")
    print(res)
