
f = open('input.txt')

scores = {
    'A': {
        'X': 3, # Loose, Rock, Scissors 3 + 0
        'Y': 4, # Draw,  Rock, Rock     1 + 3
        'Z': 8, # Win,   Rock, Paper    2 + 6
    },
    'B': {
        'X': 1, # Loose, Paper, Rock     1 + 0
        'Y': 5, # Draw,  Paper, Paper    2 + 3
        'Z': 9, # Win,   Paper, Scissors 3 + 6
    },
    'C': {
        'X': 2, # Loose, Scissors, Paper    2 + 0
        'Y': 6, # Draw,  Scissors, Scissors 3 + 3
        'Z': 7, # Win,   Scissors, Rock     1 + 6
    }
}

s = 0

while True:
    l = f.readline()
    if not l:
        break

    l = l[:-1]
    if len(l) != 3:
        break

    s += scores[ l[0] ][ l[2] ]

print(s)
