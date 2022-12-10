
f = open('input')

def unique(arr):

    t = arr.copy()
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return False

    return True

count = 0
window = ['q'] * 14

for c in f.read():

    if not c or c == "\n":
        break

    count += 1
    window = window[1:]
    window.append(c)

    if unique(window):
        print(window)
        print(count)
        break


