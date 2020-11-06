x = input()

l, f = x.rfind('h'), x.find('h')

print(x[:f+1]+ x[f+1:l][::-1] +x[l:])
