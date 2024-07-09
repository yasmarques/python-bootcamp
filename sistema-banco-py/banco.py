def menu():
    menu = """"
    ==== MENU ====

    Selecione uma opção:

    [0] Deposito
    [1] Saque
    [2] Extrato
    [3] Novo Usuário
    [4] Nova Conta
    [5] Sair
    =>"""
    return input(menu)

def depositar(saldo, deposito, extrato, /):   
        if deposito < 0:
            print("Valor de depósito invalido.")
        else:
            saldo += deposito
            extrato += f"Depósito:\tR$ {deposito:.2f}\n"
            print(f"O valor de {deposito} foi depositado na conta. Agora seu saldo é de {saldo}")
        return saldo, extrato

def sacar(*, numero_saques, limite_saques, saque, limite, saldo, extrato):
        if numero_saques < limite_saques:
            if saque < limite:
                if saldo >= saque:
                    saldo -= saque
                    extrato += f"Saque:\t\tR$ {saque:.2f}\n"
                    print("Saque realizado!")
                    numero_saques+=1
                else:
                    print("Saldo Insuficiente.")
            else:
                print(f"O valor de saque máximo é de R${limite},00")
        else:
            print("Número de saques ultrapassados")
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
         print("O CPF já está sendo usado.")
         return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (Dia - Mês - Ano): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario Criado com Sucesso.")

def filtrar_user(cpf, usuarios):
    filtro_users = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_users[0] if filtro_users else None 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
         print("Conta criada com sucesso.")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print ("Usuário não encontrado, fluxo de criação de conta encerrado.")

def main():
     
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "0":
            deposito = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
    
        elif opcao == "1":
            saque = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, limite=limite, saque = saque, extrato= extrato)

        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "3":
             criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)

        elif opcao == "5":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()