n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0
for i in score:
    i = i/max_score * 100
    
    sum += i
    
print(sum/n)