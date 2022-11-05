def etapa1(id):
    return 1000


def etapa2(votos):
    return []


def etapa3(senha):
    senhaum = str("")
    senhaum = input(f'\ndigite a senha')
    #print(senhaum[0])
    #print(senhaum.count(senhaum[0]))
    #print(senhaum.count(senhaum[1]))
    #print(senhaum.count(senhaum[2]))
    primeirocaracter = senhaum.count(senhaum[0])
    segundocaracter = senhaum.count(senhaum[1])
    terceirocaracter = senhaum.count(senhaum[2])
    ultimocaracter = senhaum.count(senhaum[-1])
    #print(ultimocaracter)
    if primeirocaracter == segundocaracter == terceirocaracter == ultimocaracter:
        print('senha válida')
    if segundocaracter != terceirocaracter:
        primeirocaracter = segundocaracter
        print(f'senha inválida')
    if primeirocaracter != segundocaracter:
        print('senha inválida')
    if ultimocaracter != primeirocaracter and segundocaracter and terceirocaracter:
        print('senha inválida')
    return False


if __name__ == "__main__":
    if etapa1('1234') > 100:
        print('ID inválido')
        exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
