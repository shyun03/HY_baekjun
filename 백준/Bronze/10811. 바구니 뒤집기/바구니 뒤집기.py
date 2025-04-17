#바구니 뒤집기

n, m = map(int, input().split())
num = []
for x in range(n):
    num.append(x+1)


for i in range(m):
    a, b = map(int, input().split())
    mat = num[a-1:b]
    
    mat.reverse()

    cnt = 0
    while(cnt<len(mat)):
        for j in range(a-1, b):
            num[j] = mat[cnt]
            cnt += 1
print(*num)

      