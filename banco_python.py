def mostrar_menu():
    print("\n--- Bem vindo ao banco python ---")
    print("1- Consultar saldo")
    print("2- Depositar")
    print("3- Sacar ")
    print("4- Ver extrato")
    print("5- Loja Python")
    print("0- Sair")

def consultar_saldo():
    print(f"Seu saldo é de R${saldo:.2f}")

def depositar_menu():
    global saldo

    while True:
      try:
          valor = float(input("Quanto você deseja depositar em R$? "))
          break
      except ValueError:
          print("Valor inválido! Digite um número!")

    if valor > 0:
          saldo += valor
          extrato.append(f"Depósito: +R${valor:.2f}")
          print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
          print("O valor precisa ser maior que zero")

def sacar_menu():
    global saldo

    while True:
      try:
          valor = float(input("Quanto você deseja sacar em R$? "))
          break
      except ValueError:
          print("Valor inválido! Digite um número!")

    if valor > 0:
          if valor <= saldo:
              saldo -= valor
              extrato.append(f"Saque: -R${valor:.2f}")
              print(f"Saque de R${valor:.2f} realizado com sucesso!")
          else:
              print("Saldo insuficiente para realizar este saque!")
    else:
          print("O valor precisa ser maior que zero")

def ver_extrato():
    print("\n========= EXTRATO ========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("===========================")

def loja_python():
    global saldo
    print("\n========= Loja Python ========")
    print("\nQuais produtos você gostaria de comprar?")
    print("1- Notebook R$5000.00")
    print("2- Celular R$3000.00")
    print("3- Televisão R$2000.00")
    opcao = input("Escolha uma opção: ")

    produto = ""
    preco = 0.0

    if opcao == "1":
        produto = "Notebook"
        preco = 5000.0
    elif opcao == "2":
        produto = "Celular"
        preco = 3000.0
    elif opcao == "3":
        produto = "Televisão"
        preco = 2000.0
    else:
        print("Opção de produto inválida!")
        return

    if saldo >= preco:
        saldo -= preco
        extrato.append(f"Compra Loja: -R${preco:.2f} ({produto})")
        print(f"{produto} comprado com sucesso!")
    else:
        print(f"Saldo insuficiente para comprar o {produto}! Seu saldo atual é de R${saldo:.2f}")


saldo = 0.0
extrato = []


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_saldo()
    elif opcao == "2":
        depositar_menu()
    elif opcao == "3":
        sacar_menu()
    elif opcao == "4":
        ver_extrato()
    elif opcao == "5":
        loja_python()
    elif opcao == "0":
        print("Obrigado por usar o Banco Python!")
        break
    else:
        print("Opção inválida!")