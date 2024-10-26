total_compras = 0 

while True:
    valor = float(input("Digite o valor da compra: R$ "))
    total_compras += valor 
    compras = input(f"essa é a ultima compra? digite 's' ou digite 'n' para o proximo valor: ").lower()
    if compras == 's':
        break
print(f"Valor total das compras: R$ {total_compras:.2f}")

fatura = total_compras
vencimento = 25
vencimento = int(input(f'digite o dia do pagamento: '))
if vencimento <= 25:
    print(f"Sua fatura é R$ {fatura:.2f}")
elif vencimento > 25:
    dias_atraso = vencimento - 25  # Calcula o número de dias de atraso
    multa = 0.01 * dias_atraso  # Multa de 1% por dia de atraso
    fatura_com_multa = fatura * (1 + multa) # Aplica a multa proporcional
    print(f"Sua fatura com {dias_atraso} dias de atraso e multa é R$ {fatura_com_multa:.2f}")