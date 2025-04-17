#알파벳 찾기

s = str(input())
t = 97
while(t<123):
    test = s.find(chr(t))
    if (test !=-1):
        print(test, end=' ')
    else:
        print(-1, end=' ')
    t+=1