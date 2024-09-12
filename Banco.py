import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#Brasil: pt_BR.UTF-8
#Estados Unidos: en_US.UTF-8
#Reino Unido: en_GB.UTF-8
#Alemanha: de_DE.UTF-8
#França: fr_FR.UTF-8
#Japão : ja_JP.UTF-8
#China  zh_CN.UTF-8
#Suíça : de_CH.UTF-8
#Índia: en_IN.UTF-8

menu = """
[1] DepositarHASJKDHSAKJHDSKJAHADSKSADDSAH DHAJDKAJSHKASHKDAHKHJDSAKH SAKJDHSAKDSDAJSHDSAHKJDSHJKDKHJS H KSAHJASKJHDSKJKDASKHJDASD
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0


def moeda_local(valor):
    return locale.currency(valor, grouping=True, symbol=True)

def data_e_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

while True:
    opcao = input(menu)

    match opcao:
        case "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"{data_e_hora()} - Depósito: {moeda_local(valor)}\n"
                print(f"Depósito de {moeda_local(valor)} realizado com sucesso!")
            else:
                print("Valor de depósito inválido.")

        case "2":
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente.")
            elif valor > limite:
                print("Saque excede o limite.")
            elif numero_saques == 3:
                print("Número máximo de saques atingido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"{data_e_hora()} - Saque: {moeda_local(valor)}\n"
                numero_saques += 1
                print(f"Saque de {moeda_local(valor)} realizado com sucesso!")
            else:
                print("Valor de saque inválido.")

        case "3":
            print("\n========== EXTRATO ====")
            print("Sem movimentações." if not extrato else extrato)
            print(f"Saldo: {moeda_local(saldo)}")
            print("=============================")

        case "4":
            break
        case _:
            print("Opção inválida.")
