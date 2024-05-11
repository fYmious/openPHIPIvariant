f = open("26.txt")
n = int(f.readline())
a = sorted([int(x) for x in f], reverse=True)

res = [a[0]]
for i in range(1, len(a)):
    if res[-1] - a[i] >= 4:
        res.append(a[i])

print(len(res), res[-1])
