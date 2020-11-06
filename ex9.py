x = input()

f, l = x.find('h'), x.rfind('h')

print(x[:f] + x[f:l] * 2 + x[l:])
