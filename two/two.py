import re


def first(input_path=""):
    with open(input_path, "r") as file:
        games = file.readlines()

    idxsum = 0
    for idx, game in enumerate(games):
        game = format_game(game)
        if check_game(game):
            idxsum += idx + 1
    return idxsum


def second(input_path="", test=None):
    if test:
        games = test
    else:
        with open(input_path, "r") as file:
            games = file.readlines()
    res = 0
    for game in games:
        game = format_game(game)
        lgame = least_cube(game)[0]
        print(lgame)
        res += lgame[0] * lgame[1] * lgame[2]
    return res


def least_cube(game):
    lgame = []
    l = [0, 0, 0]
    for r in game:
        if int(r[0]) > int(l[0]) and int(r[0]) != 0:
            l[0] = int(r[0])
        if int(r[1]) > int(l[1]) and int(r[1]) != 0:
            l[1] = int(r[1])
        if int(r[2]) > int(l[2]) and int(r[2]) != 0:
            l[2] = int(r[2])
    lgame.append(l)
    return lgame


def check_game(game):
    q = [12, 13, 14]
    for r in game:
        print(f"r: {r}")
        print(f"q: {q}")
        if int(r[0]) > int(q[0]) or int(r[1]) > int(q[1]) or int(r[2]) > int(q[2]):
            return False
    return True


def format_game(game):
    game = re.sub(r"^.*?: ", "", game).strip().split(";")
    game = [r.split(",") for r in game]
    fgame = []
    for r in game:
        fr = [0, 0, 0]
        for v in r:
            if "red" in v:
                fr[0] = int(re.search(r"\d+", v).group())
            elif "green" in v:
                fr[1] = int(re.search(r"\d+", v).group())
            elif "blue" in v:
                fr[2] = int(re.search(r"\d+", v).group())
        fgame.append(fr)
    return fgame


def sort_color(txt):
    print(txt)
    r = re.search(r"[a-zA-Z]+", txt)
    print(r.group())
    return r.group()


if __name__ == "__main__":
    # idxs = first("input.txt")
    # print(idxs)
    test = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    test = test.split("\n")[1:-1]
    print(test)
    res = second("input.txt")
    print(res)
