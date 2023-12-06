import re

def first(input_path="", test=None):
    if test is None:
        with open(input_path, "r") as file:
            lines = file.readlines()
    else:
        lines = test.split("\n")

    time = [int(x.strip()) for x in lines[0].split(":")[1].split(" ") if x != ""]
    dist = [int(x.strip()) for x in lines[1].split(":")[1].split(" ") if x != ""]
    
    races = []
    for i in range(len(time)):
        races.append((time[i], dist[i]))

    wins = 1
    for race in races:
        lwins = []
        for h in range(race[0]):
            g = button(h, race[0])
            if g > race[1]:
                lwins.append(g)
        wins *= len(lwins)
    return wins

def button(held, time):
    speed = held
    rtime = time - held
    dist = speed * rtime
    return dist

def second(input_path):

    with open(input_path, "r") as file:
        lines = file.readlines()

    time = [(x.strip()) for x in lines[0].split(":")[1].split(" ") if x != ""]
    dist = [(x.strip()) for x in lines[1].split(":")[1].split(" ") if x != ""]
    
    print(time)
    race = (int("".join(time)), int("".join(dist))) 

    wins = 1
    lwins = []
    for h in range(race[0]):
        g = button(h, race[0])
        if g > race[1]:
            lwins.append(g)
    wins *= len(lwins)

    print(wins)
    return wins


if __name__ == "__main__":
    # res = first("test.txt")
    # res = first("input.txt")
    res = second("input.txt")
    print(res)
