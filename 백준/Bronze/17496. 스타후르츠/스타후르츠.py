N, T, C, P = map(int, input().split())
#N 여름 일 수, T 자라는 일 수, C 칸의 수, P 가격

get = 0

for i in range(1,N,T):
    if (i+T) <= N:
        get+=C

money = get * P
print(money)