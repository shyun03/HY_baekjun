n = int(input())
stu = []
for i in range(n):
    stu.append([int(j) for j in input().split()])

max_fr = -1
leader = -1

for  stu_num in range(n):
    result =set()
    for grade in range(5):
        for fr in range(n):
            if stu[stu_num][grade] == stu[fr][grade]:
                result.add(fr)

    if len(result) > max_fr:
        leader = stu_num +1
        max_fr = len(result)

print(leader)
