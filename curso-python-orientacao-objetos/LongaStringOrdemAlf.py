# author andre.nascimento
def obter_mais_longa_substring(s):
    a     = list()
    for i in range(0,len(s)):
        a.append(ord(s[i]))

    b = list()
    st = ""
    st = st + chr(a[0])
    for i in range(1,len(a)):
        if (a[i] >= a[i-1]):
            st = st + chr(a[i])
            b.append(st)
        else:
            st = ""
            st = st + chr(a[i])

    imax = 0
    for i in range(0,len(b)):
        if len(b[i]) > imax:
            imax  = len(b[i])
            index = i

    return (b[index])

print(obter_mais_longa_substring('azcbobobegghakl')) #beggh
print(obter_mais_longa_substring('python')) #py
