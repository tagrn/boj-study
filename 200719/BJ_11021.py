import sys

j = int(input())
i = int(0)
sum = []
while i < j :
    a, b = map(int, sys.stdin.readline().split())
    sum.append(a+b)
    i += 1
i = int(0)
for z in sum :
    i += 1
    print(f"Case #{i}: {z}")