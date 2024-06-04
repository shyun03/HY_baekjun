n, m, l = map(int, input().split())
game = [0]*n
cnt = i = 0

while game[i] < m-1:
    game[i] += 1
    cnt += 1
    i = (i+l)%n if game[i] %2 ==1 else (i-l)%n
print(cnt)