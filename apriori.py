from itertools import combinations

items = [['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]
s = []
mv = 2


def apriori(lname, paramater):
    second = list(combinations(lname, paramater))

    slist = []
    for l in items:
        st = list(combinations(l, paramater))
        slist.append(st)

    qlist = []
    for p in slist:
        for q in p:
            qlist.append(q)

    scounts = {}
    for i in qlist:
        if i in second:
            if i in scounts:
                scounts[i] = scounts[i] + 1
            else:
                scounts[i] = 1

    for k in scounts.copy():
        if scounts[k] < mv:
            scounts.pop(k)

    return scounts


def oneElement():
    for i in items:
        for j in i:
            s.append(j)
    counts = {}
    for i in s:
        if i in counts:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
    result = sorted(counts.items(), key=lambda t: t[0], reverse=False)
    new_dict = {}
    for k, v in result:
        new_dict[k] = v

    for k in new_dict.copy():
        if new_dict[k] < mv:
            new_dict.pop(k)
    return new_dict


if __name__ == "__main__":
    new_dict = oneElement()

    nitem = []
    for k in new_dict:
        nitem.append(k)

    while True:
        n = int(input("Enter value to for combinations: "))
        support = apriori(nitem, n)
        support = sorted(support.items(), key=lambda t: t[0], reverse=False)
        print(support)
