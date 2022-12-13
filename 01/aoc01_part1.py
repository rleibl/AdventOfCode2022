
f = open("input.txt")
calories = [0]

while True:
    line = f.readline()
    if not line:
        break

    line = line[:-1]

    if line == "":
        calories.append(0)
        continue

    calories[-1] += int(line)
    

print(max(calories))
