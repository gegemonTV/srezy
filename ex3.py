x = input()

x1 = x[:len(x) // 2 if len(x) % 2 == 0 else len(x) // 2 + 1:]
x2 = x[len(x) // 2 if len(x) % 2 == 0 else len(x) // 2 + 1:] #len(x) // 2 + 1 if len(x) % 2 == 0 else len(x) // 2 + 2:]
print(x2, x1, sep='')
