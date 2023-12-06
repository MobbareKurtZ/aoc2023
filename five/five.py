import re


def first(input_path="", test=None):
    if not test:
        with open(input_path, "r") as file:
            lines = file.readlines()
    else:
        lines = test
    print(lines)

    del lines[1]

    seeds = []
    s2s = []
    s2f = []
    f2w = []
    w2l = []
    l2t = []
    t2h = []
    h2l = []
    tmp = []
    maps = []
    for line in lines:
        if not seeds:
            seeds = line
        else:
            tmp.append(line)
        if line == "\n":
            if not s2s:
                s2s = tmp[1 : len(tmp)]
                maps.append(s2s)
                tmp = []
            elif not s2f:
                s2f = tmp[1 : len(tmp)]
                maps.append(s2f)
                tmp = []
            elif not f2w:
                f2w = tmp[1 : len(tmp)]
                maps.append(f2w)
                tmp = []
            elif not w2l:
                w2l = tmp[1 : len(tmp)]
                maps.append(w2l)
                tmp = []
            elif not l2t:
                l2t = tmp[1 : len(tmp)]
                maps.append(l2t)
                tmp = []
            elif not t2h:
                t2h = tmp[1 : len(tmp)]
                maps.append(t2h)
                tmp = []

    h2l = tmp[1 : len(tmp)]
    maps.append(h2l)
    # seeds = [[seed.strip()] * 8 for seed in seeds.split(":")[1].split(" ")[1:]]
    seeds = [seed.strip() for seed in seeds.split(":")[1].split(" ")[1:]]
    print(seeds)
    l = len(seeds) / 2
    nseeds = []
    for i in range(int(l)):
        nseeds += list(range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))
    print(nseeds)

    for i, s in enumerate(nseeds):
        nseeds[i] = [s] * 8
    print(nseeds)
    seeds = nseeds

    for idx, map in enumerate(maps):
        convert_map(map, seeds, idx + 1)
    print(seeds)

    res = min([x[-1] for x in seeds])
    return res


def convert_map(map, seeds, idx):
    for c in map[0:-1]:
        c = c.strip().split(" ")
        for seed in seeds:
            if seed[idx] == seed[idx - 1]:
                if int(c[1]) <= int(seed[idx - 1]) and int(seed[idx - 1]) <= int(
                    c[1]
                ) + int(c[2]):
                    tmp = int(seed[idx - 1]) + (int(c[0]) - int(c[1]))
                    # print(
                    #     f"MATCH HÄR: {int(seed[idx-1])}, på intervall {c[1]}-{int(c[1])+int(c[2])}.    Jag är på {idx}   Jag blir: {tmp}"
                    # )
                    seed[idx:] = [tmp] * (len(seed) - idx)
                else:
                    seed[idx] = seed[idx - 1]


if __name__ == "__main__":
    res = first("test.txt")
    # res = first("input.txt")
    print(res)
