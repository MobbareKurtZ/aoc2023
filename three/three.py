import re
from pprint import pp


def first(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            schem = file.readlines()
    else:
        schem = test.split("\n")
    global disc
    disc = [["."] * len(schem[0]) for i in range(len(schem))]
    res = 0
    for idx, l in enumerate(schem):
        print("NEW LINE")
        matches = re.finditer(r"[^a-zA-Z0-9.\n]+", l)
        if matches:
            for match in matches:
                midx = match.start()
                print("--------------NEW MATCH---------------")
                print(match)
                lsum = search_symb(midx, idx, schem)
                res += lsum
    res = 0
    for l in disc:
        s = "".join(l)
        s = s.split(".")
        s = sum(int(x) for x in s if x.isdigit())
        res += s

    return res


def search_symb(midx, idx, schem):
    lsum = 0
    for i in range(3):
        for j in range(3):
            if (
                idx + i > 0
                and idx - 1 + i < len(schem)
                and midx + j > 0
                and midx - 1 + j < len(schem[idx - 1 + i])
            ):
                print(f"Looking at {idx-1+i}, {midx-1+j}")
                c = schem[(idx - 1 + i)][midx - 1 + j]
                print(c)
                if c.isdigit():
                    num = search_number(schem[idx - 1 + i], midx - 1 + j, idx - 1 + i)
                    lsum += int(num)
    return lsum


def search_number(line, idx, lidx):
    i = 0
    fi = 0
    li = 0
    while True:
        if not line[idx - i].isdigit() or idx - i < 0:
            fi = idx - i + 1
            break
        i += 1
    i = 0
    while True:
        if idx + i > len(line) - 1 or not line[idx + i].isdigit():
            li = idx + i
            break
        i += 1
    num = line[fi:li]
    if disc[lidx][fi:li] != num:
        disc[lidx][fi:li] = num
        print(f"Found: {num}")
        return num
    print(f"Found already found: {num}")
    return 0


def second(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            schem = file.readlines()
    else:
        schem = test.split("\n")

    global disc
    disc = [["."] * len(schem[0]) for i in range(len(schem))]
    res = 0
    for idx, l in enumerate(schem):
        matches = re.finditer(r"[^a-zA-Z0-9.\n]+", l)
        if matches:
            for match in matches:
                midx = match.start()
                if match.group() == "*":
                    print(res)
                    res += search_symb2(midx, idx, schem)
    pp(disc)
    return res


def search_symb2(midx, idx, schem):
    count = 0
    cur = 1
    num = 0
    for i in range(3):
        for j in range(3):
            if (
                idx + i > 0
                and idx - 1 + i < len(schem)
                and midx + j > 0
                and midx - 1 + j < len(schem[idx - 1 + i])
            ):
                # print(f"Looking at {idx-1+i}, {midx-1+j}")
                c = schem[(idx - 1 + i)][midx - 1 + j]
                if c.isdigit():
                    num = search_number2(schem[idx - 1 + i], midx - 1 + j, idx - 1 + i)
                    print(f"MULT: {cur}*{int(num)}")
                    cur *= int(num)
                    if int(num) != 1:
                        count += 1
                    if count == 2:
                        pass
                    elif count > 2:
                        cur = 0
    if count == 2:
        return cur
    else:
        return 0


def search_number2(line, idx, lidx):
    i = 0
    fi = 0
    li = 0
    while True:
        if not line[idx - i].isdigit() or idx - i < 0:
            fi = idx - i + 1
            break
        i += 1
    i = 0
    while True:
        if idx + i > len(line) - 1 or not line[idx + i].isdigit():
            li = idx + i
            break
        i += 1
    num = line[fi:li]
    if "".join(disc[lidx][fi:li]) != num:
        disc[lidx][fi:li] = num
        return num
    return 1


if __name__ == "__main__":
    test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    #     test = """12.......*..
    # +.........34
    # .......-12..
    # ..78........
    # ..*....60...
    # 78.........9
    # .5.....23..$
    # 8...90*12...
    # ............
    # 2.2......12.
    # .*.........*
    # 1.1..503+.56"""

    #     test = """........
    # .24..4..
    # ......*."""
    # res = first("input.txt", test)
    # res = first("input.txt")
    # res = second("input.txt", test)
    res = second("input.txt")
    print(res)
