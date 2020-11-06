x = input()
f, l = x.find('h'), x.rfind('h')

print(x[:f]+x[l+1::])
