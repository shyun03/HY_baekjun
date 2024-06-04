H, M = map(int, input().split())
if M>=45:
    if M-45 == 0:
        print(H, 0)
    else:
        print(H, M-45)
else:
    R = 45-M
    if H-1 == -1:
        print(23, 60-R)
    else:
        print(H-1,60-R)