n = int(input())
a = n- 1 #중소형 불꽃 수

#충족 방정식 k**2 + k == a
k=0
while True:
    k+=1
    if k**2 + k ==a:
        print(k)
        break
