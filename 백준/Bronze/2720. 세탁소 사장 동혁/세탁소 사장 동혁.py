t = int(input())
for i in range(t):
    money = int(input())
    q = money // 25
    money = money - q*25
    d  = money // 10
    money = money -d*10
    n = money // 5
    p = money - n*5
    print(q, d, n, p)