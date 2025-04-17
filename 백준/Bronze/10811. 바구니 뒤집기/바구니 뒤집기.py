#바구니 뒤집기 코드 줄이기

n, m = map(int, input().split())
num = []
for x in range(n):
    num.append(x+1)


for i in range(m):
    a, b = map(int, input().split())
    num[a-1:b] = reversed(num[a-1:b])
    

print(*num)