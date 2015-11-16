data = open("test.txt", 'r')
G = {}

for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]

print G[0]
