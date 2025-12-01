with open("task.txt") as f:
    rows = [(r[0],int(r[1:].strip())) for r in f.readlines()]

q=0
w=0
pos = 50
for i, (direct, amount) in enumerate(rows):
    d = 0
    prev_pos = pos
    pos += amount * (-1)**(direct=='L')
    if pos < 0:
        d =abs(pos)//100+1
        if prev_pos == 0:
            d-=1
        print(i+1,prev_pos, pos, d)
        w+=d
    if pos > 100:
        d = pos//100
        print(i+1,prev_pos, pos, d)
        w += d
    pos%=100
    if pos == 0 and d == 0:
        print(i+1, prev_pos, pos, '0')
        q+=1
print(q+w)
#5157<answer<6200
