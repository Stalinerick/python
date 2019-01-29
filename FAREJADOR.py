from os import listdir
from os.path import isfile, join
palavra1 = ['/NOTO','/NOAL','/NODI','/NOSA','/DTPO','/DTPU','/DTMC','/DTJS','/DTJB','/DTDV','/DTDT','/DTCL','/DTCA','/DTBD','/DTAL','/DTVR','/DTUA','/DTTO','/DTSS','/DTSA','/DTRC','/DTPM','/DTLP','/DTLV','/DTVA','/DTFL','/DTCV','/DTAX','/DTBE','/DTCN','/DTIB','/DTLS','/DTRN','/DTSZ','/DTLE']
p = []
def procura():
    decisao = input('Deseja uma procura personalizada [1]Sim e [2]Não?')
    if(decisao == '1'):
        palavra0 = input('Digite a palavra que será procurada: ')
        with open('salvo.txt','w') as b0:
            salvo0 = b0.read()
        with open(arquivo) as f:
            b0 = open(arquivo)
            encontrada0 = f.read().count(palavra0)
            salvar0 = open('salvo.txt','w')
            texto0 = str(salvo0)+"\nProcura personalizada Encotrado: "+palavra0+" Na quantidade "+str(encontrada0)
            salvar0.write(texto0)
            salvar0.close()
    else:
        print('Ok... finalizando')
def pega1(arquivo, pastas, tipo):
    quant = len(palavra1)
    x = 0
    while(x<quant):
        palavra = palavra1[x]
        x=x+1
        with open('salvo.txt') as b:
            salvo2 = b.read()
        with open(arquivo) as f:
            b = open(arquivo)
            encontrada1 = f.read().count(palavra)
            if(encontrada1>0):
                salvar = open('salvo.txt','w')
                texto1 = str(salvo2)+"\n"+tipo+"	"+pastas+"	"+palavra+"	"+str(encontrada1)
                salvar.write(texto1)
                salvar.close()
            else:
                pass
def entrada():
    mypath = input("Qual pasta você deseja scanear? ")
    vasc=0
    scan_all(mypath, vasc)
def scan_all(mypath, vasc):
    onlyfiles = [f for f in listdir(mypath)]
    contar = int(len(onlyfiles))
    contagem(mypath,onlyfiles,contar)
def contagem(mypath,onlyfiles,contar):
    print(mypath,onlyfiles,contar)
    i = 0
    while i < contar:
        arquivo = onlyfiles[i]
        pastas = arquivo
        if ('fatura' in pastas):
            tipo = 'FATURA'
        elif ('boletim' in pastas):
            tipo = 'BOLETIM'
        elif ('fatdive' in pastas):
            tipo = 'FATDIVE'
        elif ('demdebi' in pastas):
            tipo = 'DEMDEBI'
        else:
            tipo = 'NULL'
        cod = pastas.find('g')
        pastas = pastas[cod:(cod+4)]
        arquivo = mypath+"/"+arquivo
        if('.txt' in arquivo):
            with open('salvo.txt') as bS:
                salvoS = bS.read()
            with open(arquivo) as f:
                salvarS = open('salvo.txt','w')
                textoS = str(salvoS)+"\nARQUIVO	GRUPO	DISTRITO	QUANTIDADE"   
                salvarS.write(textoS)
                salvarS.close()
            
            pega1(arquivo, pastas, tipo)
            i = i+1
            print("scan completo \n Arquivo: "+str(i)+" De: "+str(contar)+"Nome: "+pastas)
        else:
            i = i+1
            print("indo ao proximo \n Arquivo: "+str(i)+" De: "+str(contar)+"Nome: "+pastas)
    else:
        i = i+1
        print("Saindo da pasta...")
while True:
    entrada()

                    

