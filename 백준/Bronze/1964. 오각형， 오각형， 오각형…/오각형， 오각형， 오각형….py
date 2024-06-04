n = int(input())
dot = 5
po = 7

for i in range(1, n):
    dot += po
    po +=3

print(dot%45678)