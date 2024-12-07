
with open('./input.txt') as f:
    
    locations = f.readlines()

left = []
right = []
freq = {}

for line in locations:
    tmp = line.split()
    left.append(int(tmp[0]))
    right.append(int(tmp[1]))

# left.sort()
# right.sort()

for r in right:
    if r in freq:
        freq[r] = freq[r] + 1
    else:
        freq[r] = 1

accum = 0
for l in left:
    if l in freq:
        accum = accum + (freq[l] * l)

print("Answer: ", accum)