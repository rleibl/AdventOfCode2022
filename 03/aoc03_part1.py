
f = open('input')
data = f.readlines()

sum_of_priorities = 0

for line in data:

    line = line[:-1] # chomp
    if not line:
        break

    l = int(len(line)/2)

    left = line[:l]
    right = line[l:]

    match = [ i for i in left if i in right ][0]

    val = 0
    if ord(match) < ord('a'):
        val = ord(match) - ord('A') + 27
    else:
        val = ord(match) - ord('a') + 1

    sum_of_priorities += val

print(sum_of_priorities)

