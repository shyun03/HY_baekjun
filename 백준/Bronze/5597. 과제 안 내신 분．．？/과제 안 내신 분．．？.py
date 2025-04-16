#과제 안 내신 분
num = []
for x in range(30):
    num.append(x+1) 
for i in range(28):
    a = int(input())
    for i in num:
        if(i == a):
            num.remove(i)

print(num[0])
print(num[1])