with open("task.txt") as f:
    rows = [r.strip() for r in f.readlines()]
batteries = [[int(i)for i in r]for r in rows]

print(batteries)
s = 0

max_numbers = []
for i, b in enumerate(batteries):
    numbers=[]
    better_number = []
    index_max_number=-1
    for a in range(12):
        end_range = -(11-a)
        if end_range == 0:
            watch = b[index_max_number+1:]
        else:
            watch = b[index_max_number+1:end_range]
        max_number = max(watch)
        watch_end = b[index_max_number+1:]
        index_max_number = watch_end.index(max_number)+index_max_number+1
        better_number.append(max_number)
        print(index_max_number, max_number, better_number, watch, len(watch), watch_end, len(watch_end))

    max_numbers.append(int(''.join(str(i) for i in better_number)))
    print(i,len(batteries))
print(sum(max_numbers))