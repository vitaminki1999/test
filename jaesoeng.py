while 1:

    n = input()
    if int(n) == 0:
        break

    b = list(n)
    v = 0
    for i in range(len(b)):
        if b[i] == 1:
            v += 2
        elif b[i] == 0:
            v += 4
        else:
            v += 3
    print(v+len(b))
print(len(b)+1)