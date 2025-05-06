def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    resultado = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
        valor = valor % cedula

    return resultado

def menu():
    print("=" * 40)
    print("        BEM-VINDO AO BANCO CIRROSE")
    print("=" * 40)

while True:
    menu()
    try:
        valor = int(input("Digite o valor para saque (0 para sair): R$ "))
        if valor == 0:
            print("Encerrando operação. Obrigado por usar o Banco CIRROSE!")
            break
        elif valor < 0:
            print("⚠️ Valor inválido. Digite um número positivo.\n")
            continue

        cedulas = calcular_cedulas(valor)

        print("\n💸 Cédulas entregues:")
        for cedula, qtd in cedulas.items():
            print(f"➡️ {qtd} cédula(s) de R$ {cedula}")
        print()

    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números inteiros.\n")