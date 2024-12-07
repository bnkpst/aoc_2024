
with open('./input.txt') as f:
    
    locations = f.readlines()

diffs = []
left = []
right = []

for line in locations:
    tmp = line.split()
    left.append(int(tmp[0]))
    right.append(int(tmp[1]))

left.sort()
right.sort()


for l, r in zip(left, right):
    diffs.append(abs(l - r))

sum = sum(diffs)

print("Answer: ", sum)
    


