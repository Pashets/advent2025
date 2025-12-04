with open("task.txt") as f:
    rows = [r.strip() for r in f.readlines()]
batteries = [[int(i)for i in r]for r in rows]

print(batteries)
s = 0
max_numbers = []
for b in batteries:
    numbers=[]
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            numbers.append(int(f'{b[i]}{b[j]}'))
    max_numbers.append(max(numbers))
print(sum(max_numbers))