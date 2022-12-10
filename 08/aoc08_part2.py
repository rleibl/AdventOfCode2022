
forest = []

f = open('input')
#f = open('example')
for l in f.readlines():
    if not l or l == "\n":
        break
    l = l[:-1]

    row = []
    for e in l:
        row.append(int(e))

    forest.append(row)

length = len(forest)

scenic_arr = []

for x in range(1, length-1):
    for y in range(1, length-1):

        height = int(forest[y][x]) # note that x and y are flipped in forest
        print(f'Looking at [{x},{y}]. Height is {height} ')

        scenic_top   = 0
        scenic_bot   = 0
        scenic_left  = 0
        scenic_right = 0

        # to the top 
        for i in range(y-1, -1, -1):
            scenic_top += 1
            if forest[i][x] >= height:
                break

        # to the bottom
        for i in range(y+1, length):
            scenic_bot += 1
            if forest[i][x] >= height:
                break

        # to the left
        for i in range(x-1, -1, -1):
            scenic_left += 1
            if forest[y][i] >= height:
                break

        # to the right
        for i in range(x+1, length):
            scenic_right += 1
            if forest[y][i] >= height:
                break

        scenic_arr.append(scenic_top * scenic_bot * scenic_left * scenic_right)

scenic_arr.sort()

print(scenic_arr)
