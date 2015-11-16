data = open("test.txt", 'r')
G = {}
lst = []

for line in data:
    lst = [tuple(s.split(',')) for s in line.split()]
    G[int(lst[0][0])] = lst[1:]
