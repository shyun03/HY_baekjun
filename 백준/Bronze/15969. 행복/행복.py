n = int(input())
cmp = 0
while True:
    alist = [int(x) for x in input().split()]
    if len(alist) == n:
        alist.sort() #정렬
        cmp = int(alist[n-1] - alist[0])
        break
    else:
        break

print(cmp)