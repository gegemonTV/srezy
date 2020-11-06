x = input()
for i in range(len(x)):
    n = x[i] if i%3 !=0 else ''
    print(n, end='')
