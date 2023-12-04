import re


def first(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            schem = file.readlines()
    else:
        schem = test.split("\n")
    global disc
    disc = [[] for i in range(len(schem))]
    res = 0
    for idx, l in enumerate(schem):
        matches = re.finditer(r"[^a-zA-Z0-9.\n]+", l)
        if matches:
            for match in matches:
                midx = match.start()
                print(match)
                # print(
                #     f"{schem[(idx - 1)][midx - 1]}{schem[(idx-1)][midx]}{schem[(idx - 1)][midx + 1]}"
                # )
                # print(
                #     f"{schem[(idx)][midx - 1]}{schem[(idx)][midx]}{schem[(idx)][midx + 1]}"
                # )
                # print(
                #     f"{schem[(idx + 1)][midx - 1]}{schem[(idx+1)][midx]}{schem[(idx + 1)][midx + 1]}"
                # )
                lsum = search_symb(midx, idx, schem)
                res += lsum
    return res


def search_symb(midx, idx, schem):
    lsum = 0
    for i in range(3):
        for j in range(3):
            if idx - 1 + i < len(schem) and midx - 1 + j < len(schem[idx - 1 + i]):
                c = schem[(idx - 1 + i)][midx - 1 + j]
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
        if not line[idx + i].isdigit() or idx + i > len(line) - 1:
            li = idx + i
            break
        i += 1
    num = line[fi:li]
    print(num)
    if num not in disc[lidx]:
        disc[lidx].append(num)
        return num
    return 0


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
    #     test = """........
    # .24..4..
    # ......*."""
    # res = first("input.txt", test)
    res = first("input.txt")
    print(res)
