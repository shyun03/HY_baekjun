N = int(input()) # 학생 수

student= list(map(int, input().split()))


if(student.count(0) >= N/2): #절반 이상 기권
    print("INVALID")
else:
    t = student.count(1)
    f = student.count(-1)
    if (t>f):
        print("APPROVED")
    elif(t<=f):
        print("REJECTED")