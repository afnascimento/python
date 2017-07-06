def numero_perfeito(num):
    count = 1
    soma = 0
    while count < num:
        if (num % count) == 0:
            soma = soma + count
            count = count + 1
        else:
            count = count + 1

    if (soma == num):
        return True
    else:
        return False

numero = 28
perfeito = numero_perfeito(numero)
if (perfeito):
    print(numero, "numero perfeito")
else:
    print(numero, "numero imperfeito")