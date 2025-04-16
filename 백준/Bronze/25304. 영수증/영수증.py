#영수증
#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액

x = int(input())
n = int(input())
count = 0
result = 0

while(True):
    a, b = map(int, input().split())
    result += a * b
    count +=1
    
    if(count == n):
        break

if (x == result):
    print("Yes")
else:
    print("No")