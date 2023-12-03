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
                lsum = search_symb(midx, idx, schem)
                res += lsum
    return res


def search_symb(midx, idx, schem):
    lsum = 0
    for i in range(3):
        for j in range(3):
            c = schem[idx - 1 + i][midx - 1 + j]
            if c.isdigit():
                num = search_number(schem[idx - 1 + i], midx - 1 + j, idx - 1 + i)
                lsum += int(num)
    return lsum


def search_number(line, idx, lidx):
    s = line[max(idx - 2, 0) : min(idx + 3, len(line))]
    num = re.findall(r"\d+", s)
    num = max(num)
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
    test = """..........................................704..................283.328..........................218.............744.................82......
............687..320.....518......*.............*.*.....#...........2...&...*...........*..19.356*......313.994.467..984...+................
........................................782...............665......................532.......................998...991.702.542....406.779..."""
    res = first("input.txt", test)
    print(res)
