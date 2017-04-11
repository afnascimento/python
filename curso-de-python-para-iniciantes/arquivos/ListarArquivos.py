import os

def listarArquivosDiretorio(diretorio):
    for f in os.listdir(diretorio):
        print(f)

listarArquivosDiretorio('C:\Windows')