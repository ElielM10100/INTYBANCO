from banco import obterconta , banco

def transferir(contari:int,contades:int, valor:float)-> None:
    contaorigem=obterconta(contari)
    contadestino=obterconta(contades)
    if contaorigem and contadestino:
        if  contaorigem ['saldo'] >=valor:
            contaorigem['saldo'] -=valor
            contadestino['saldo']+=valor
            print('Transferencia realizada com sucesso!!')
        else:
            print('saldo insuficiente')
    else:
        print('uma ou mais contas nao existem')

if __name__=='__main__':
    transferir(1,2,158.99)
    print(banco)