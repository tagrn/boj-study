j = int(input())
i = int(0)
while i < j :
    i += 1
    x = j - i
    z = int(0)
    while z < x :
        print(" ", end='')
        z += 1
    z = int(0)
    while z < i :
        print("*", end='')
        z += 1
    print('')