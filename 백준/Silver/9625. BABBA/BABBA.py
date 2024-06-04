k = int(input())

cnt = [0] * (k+1)
cnt[1] = 1 #1까지의 dafault

#2부터 규칙 (피보나치)
for i in range(2, k+1):
    cnt[i] = cnt[i-1] + cnt[i-2]

print(cnt[k-1], cnt[k])