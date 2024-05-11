with open("9.txt", 'r') as file:
    table = [sorted([int(j) for j in i.split()]) for i in file]

def odin(row):
    return row[3] < (row[0] + row[1] + row[2])

def dva(row):
    return (row[0] + row[3]) == (row[1] + row[2])

k = 0
for row in table:
    if odin(row) and dva(row):
        k += 1

print(k)
