st = open("24.txt", 'r').readline().replace("R", "Q").replace("W", "Q").replace("2", "1").replace("4", "1")

c, m = 1, 0
for i in range(1, len(st)):
    if st[i - 1] + st[i] not in ["QQ", "11"]:
        c += 1
        m = max(m, c)
    else:
        c = 1

print(m)

while "QQ" in st: st = st.replace("QQ", "Q Q")
while "11" in st: st = st.replace("11", "1 1")

print(max(len(c) for c in st.split()))
