import re


def part_one(input_path):
    with open(input_path, "r") as file:
        cals = file.readlines()
    val = 0
    for cal in cals:
        ds = re.findall(r"\d", cal)
        d = int(f"{ds[0]}{ds[-1]}")
        val += d

    return val


def part_two(input_path="", test=None):
    if input_path != "":
        with open(input_path, "r") as file:
            cals = file.readlines()
    else:
        cals = test
    val = 0
    for cal in cals:
        cal = t2d(cal)
        ds = re.findall(r"\d", cal)
        d = int(f"{ds[0]}{ds[-1]}")
        val += d

    return val


def t2d(txt):
    td = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 0
    s = ""
    ns = txt
    while i < len(txt):
        s += txt[i]
        m = None
        for idx, t in enumerate(td):
            m = re.search(rf"{re.escape(t)}", s)
            if m:
                ns = re.sub(rf"{m.group()}", str(idx + 1) + m.group()[-1], ns)

        i += 1
    return ns


if __name__ == "__main__":
    # val = part_one("input.txt")
    # print(val)
    # val = part_two("input.txt")
    # print(val)
    test = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    # print(part_two("", test))
    print(part_two("input.txt"))
