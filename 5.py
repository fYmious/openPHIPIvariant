def f(n):
    bn = f"{n:b}"
    if n % 2 == 0: bn = "10" + bn
    else: bn = "1" + bn + "01"
    return int(bn, 2)

for n in range(1, 10_000):
    r = f(n)
    if r > 516:
        print(n)
        break
