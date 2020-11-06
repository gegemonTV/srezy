n = int(input())

for i in range(n+1):
    print('|' + ' '*(len(str(n))-len(str(n))) + str(i) + '|' + ' '*(len(str(n*n))-len(str(i*i))) + str(i*i) + '|' + ' '*(len(str(n*n*n))-len(str(i*i*i))) + str(i*i*i) + '|')
