class SaqueError(Exception):
    pass

class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def saque(self, valor):
        saldo_temp = (self.saldo - valor)
        if saldo_temp <= 0:
            msg = 'sem saldo suficiente para sacar R$%d' % (valor,)
            raise SaqueError(msg)
        else:
            self.saldo -= valor
            print('saque', valor)

    def deposito(self, valor):
        self.saldo += valor
        print('deposito', valor)

try:
    c = ContaBancaria()
    c.deposito(100)
    c.saque(70)
    c.saque(40)
except SaqueError as error:
    print('erro ocorrido', error)