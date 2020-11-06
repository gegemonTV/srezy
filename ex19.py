n = int(input())

for i in range(n+1):
    s = '|' + ' '*(10-len(str(i)))+str(i)+'|'+' '*(10-len(str(i*i)))+str(i*i)+'|'+' '*(10-len(str(i*i*i)))+str(i*i*i)+'|'
    print(s)
