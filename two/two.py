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
    idxs = first("input.txt")
    print(idxs)
