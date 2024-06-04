T = int(input())

for i in range(T):
    sum1 = 0 
    n, m = map(int, input().split())
    for j in range(n, m+1):
        z = str(j)
        sum1 += z.count('0')  #count함수 해당 문자의 개수를 셈
    print(sum1)