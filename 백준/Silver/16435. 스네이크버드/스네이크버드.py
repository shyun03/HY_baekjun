N , L = map(int,input().split())  
h = list(map(int,input().split()))

h.sort()  #정렬

for i in h:                 
    if i <= L:                     
        L += 1                 
print(L) 