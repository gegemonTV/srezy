d=int(input())
n = int(input())

for i in range(n+1):
    for j in range(1, d+1):
        print('|' + ' '*(len(str(n**j))-len(str(i**j))) + str(i**j), end = '')
    print('|')
