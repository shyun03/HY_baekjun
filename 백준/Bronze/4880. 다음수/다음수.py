while True:
    a1, a2, a3 = map(int, input().split())
    if(a1==a2==a3):
        break
    else:
        if a2 - a1 == a3 - a2:
            d = a3-a2
            a4 = a3+d
            print("AP", a4)
        else:
            if a2//a1 == a3//a2:
                r = a3//a2
                a4 = a3*r
                print("GP", a4)