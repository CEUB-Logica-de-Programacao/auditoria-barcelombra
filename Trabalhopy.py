voto_list = []
votostr = ''
votos = []
numvotos=[]
while True:
    voto = int(input('Declare seu ID:\n'))
    if voto>=1000 and voto<=9999:
        print('ID válido')
        break
    else:
        print('ID inválido')
new1=slice(0,2)
new2=slice(2,4)
votostr = str(voto)

totalvotos = int(input(f'qual o total de votos?\n'))
for i in range(1,totalvotos+1): # type: ignore
    teste=0
    numvotosinput=((input('Votos computados:\n')))
    numvotos.append(numvotosinput)
for i in range(1,totalvotos+1):
    votosinput=input(('Insira o voto para testá-lo:\n'))
    votos.append(votosinput)
#print(votos,numvotos,f'{votos in numvotos}',type(votos))
def Diff(votos, numvotos):
    return (list(list(set(numvotos)-set(votos))))
if votos == numvotos:
    print('Todos os votos são válidos')
else:
    print(f'\nOs seguintes votos não são válidos {(Diff(numvotos, votos))}')
senhaum = str("")
senhaum = input(f'\nDigite a senha: \n')
primeirocaracter = senhaum.count(senhaum[0])
segundocaracter = senhaum.count(senhaum[1])
terceirocaracter = senhaum.count(senhaum[2])
ultimocaracter = senhaum.count(senhaum[-1])
if primeirocaracter == segundocaracter == terceirocaracter == ultimocaracter:
    print('senha válida')
if segundocaracter != terceirocaracter:
    primeirocaracter = segundocaracter
    print(f'senha inválida')
if primeirocaracter != segundocaracter:
    print('senha inválida')
if ultimocaracter != primeirocaracter and segundocaracter and terceirocaracter:
    print('senha inválida')
