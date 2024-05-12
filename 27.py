f = open("27A.txt")
n = int(f.readline())
a = [int(x) for x in f]

mn = float("inf")
for i in range(len(a)):
    s = 0
    for j in range(len(a)):
        r = min(abs(i - j), n - abs(i - j))
        s += a[j] * r
    mn = min(mn, s)

print(mn)