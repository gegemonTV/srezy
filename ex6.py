x = input()
c = x.find('f')

if c == -1:
    print(-2)
elif c!=-1:
    n = x.find('f', c+1)
    if n == -1:
        print(-1)
    else:
        print(n)

