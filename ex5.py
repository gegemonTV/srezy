s = input()
if s.find('f') == s.rfind('f') != -1:
    print(s.find('f'))
elif s.find('f') != s.rfind('f'):
    print(s.find('f'), s.rfind('f'))
