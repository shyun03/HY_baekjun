#공넣기
#n은 바구니 수, m은 횟수
n, m = map(int, input().split())
list = [0 for x in range(n)]
for c in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        list[x] = k
print(*list)