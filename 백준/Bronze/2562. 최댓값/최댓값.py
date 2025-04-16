#최댓값
num = []
for i in range(9):
    a = int(input())
    num.append(a)
    
m = max(num)

print(m)
print(num.index(m)+1)