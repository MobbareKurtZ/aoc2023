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
    print(input_path)
    if input_path != "":
        with open(input_path, "r") as file:
            cals = file.readlines()
    else:
        cals = test
    td = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    val = 0
    for cal in cals:
        ds = re.findall(r"\d|" + "|".join(td), cal)
        f = ds[0] if len(ds[0]) == 1 else td.index(ds[0]) + 1
        l = ds[-1] if len(ds[-1]) == 1 else td.index(ds[-1]) + 1
        d = int(f"{f}{l}")
        val += d

    return val


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
