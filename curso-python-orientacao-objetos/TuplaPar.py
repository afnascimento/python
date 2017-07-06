def tupla_par(tupla):
    tupleTemp = []
    for index, element in enumerate(tupla):
        if index % 2 == 0:
            tupleTemp.append(element)
    return tupleTemp

def tupla_par2(tupla):
    return tupla[0::2]

tupla = ('oi', 'estou', 'estudando', 'poo')
print(tupla_par(tupla))

tupla = (1, 'teste', 3, 'poo')
print(tupla_par2(tupla))