def imprime_nome(nome):
    print(nome)

print('imprime_nome')
imprime_nome('Andre')

def imprime_nome_sobrenome(nome, sobrenome):
    print(nome, sobrenome)
print('imprime_nome_sobrenome')
imprime_nome_sobrenome('Andre', 'Nascimento')

def nome_completo_usuario(codigo):
    if codigo == 10:
        return 'Andre', 'Nascimento'
print('nome_completo_usuario')
nome, sobrenome = nome_completo_usuario(10)
print(nome, sobrenome)