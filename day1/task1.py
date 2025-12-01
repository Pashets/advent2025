with open("task.txt") as f:
    rows = [(r[0],int(r[1:].strip())) for r in f.readlines()]

q=0
pos = 50
for direct, amount in rows:
    pos += amount * (-1)**(direct=='L')
    pos%=100
    if pos == 0:
        q+=1
print(q)
