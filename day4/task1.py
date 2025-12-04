with open("task.txt") as f:
    rows = [i.strip() for i in f.readlines()]
print(rows)
q = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j]=='.':continue
        ys_show = [i]
        if i!=0:
            ys_show.append(i-1)
        if i!=len(rows)-1:
            ys_show.append(i+1)
        xs_show = [j]
        if j!=0:
            xs_show.append(j-1)
        if j!=len(rows)-1:
            xs_show.append(j+1)
        coords_sep = [(x,y) for x in xs_show for y in ys_show if (x,y)!=(j,i)]
        values_sep = [rows[y][x]for (x,y) in coords_sep]
        print(j,i,xs_show,ys_show,coords_sep,values_sep)
        if values_sep.count('@')<4:
            print(j,i)
            q+=1
print(q)