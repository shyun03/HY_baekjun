n = int(input())
c = [int(input()) for _ in range(n)]

l_c = r_c = 0
l_m = r_m = 0

for i in c:
     if i > l_m:
         l_m = i
         l_c+=1
for i in c[::-1]:
     if i>r_m:
         r_m = i
         r_c+=1

print(l_c)
print(r_c)