x = input()

f, l = x.find('h'), x.rfind('h')

print(x[:f+1] + x[f+1:l-1].replace('h', 'H') + x[l-1:])

