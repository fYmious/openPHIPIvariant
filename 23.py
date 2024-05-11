def f(curr, end, q):
    if curr > end: return 0
    if curr == end: return 11 in q and 13 in q
    if curr < end: return f(curr + 1, end, q + [curr]) + f(curr + 2, end, q + [curr]) + f(curr * 2, end, q + [curr])

print(f(4, 15, []))
