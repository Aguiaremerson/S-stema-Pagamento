print("=== FORMAS DE PAGAMENTO ===")

gasto = float(input("Digite o valor da compra: R$ "))

print("""
[1] À vista dinheiro ou cheque (10% de desconto)
[2] À vista cartão (5% de desconto)
[3] 2x no cartão (sem juros)
[4] 3x ou mais no cartão (20% de juros)
""")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    total = gasto - (gasto * 0.10)
    print(f"Sua compra ficará em R$ {total:.2f}")

elif opcao == 2:
    total = gasto - (gasto * 0.05)
    print(f"Sua compra ficará em R$ {total:.2f}")

elif opcao == 3:
    total = gasto
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f}")

elif opcao == 4:
    total = gasto + (gasto * 0.20)
    totalparce = int(input("Quantas parcelas? "))
    parcela = total / totalparce
    print(f"Sua compra parcelada em {totalparce}x de R$ {parcela:.2f} com juros")
    print(f"Total da compra: R$ {total:.2f}")

else:
    print("Opção inválida!")
