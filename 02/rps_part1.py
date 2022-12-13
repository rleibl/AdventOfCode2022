
f = open('input.txt')

scores = {
    'A X': 4, # Rock, Rock     1 + 3
    'A Y': 8, # Rock, Paper    2 + 6
    'A Z': 3, # Rock, Scissors 3 + 0

    'B X': 1, # Paper, Rock     1 + 0
    'B Y': 5, # Paper, Paper    2 + 3
    'B Z': 9, # Paper, Scissors 3 + 6

    'C X': 7, # Scissors, Rock     1 + 6
    'C Y': 2, # Scissors, Paper    2 + 0
    'C Z': 6, # Scissors, Scissors 3 + 3
}

s = 0

while True:
    l = f.readline()
    if not l:
        break

    l = l[:-1]
    if len(l) != 3:
        break

    s += scores[l]

print(s)
