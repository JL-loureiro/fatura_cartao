total_compras = 0 

while True:
    valor = float(input("Digite o valor da compra: R$ "))
    total_compras += valor 
    compras = input("Essa é a última compra? Digite 's' ou digite 'n' para o próximo valor: ").lower()
    if compras == 's':
        break
print(f"Valor total das compras: R$ {total_compras:.2f}")
fatura = total_compras
vencimento = 25
vencimento = int(input("Digite o dia do pagamento: "))
if vencimento <= 25:
    print(f"Sua fatura é R$ {fatura:.2f}")
else:
    dias_atraso = vencimento - 25
    multa = 0.01 * dias_atraso
    fatura_com_multa = fatura * (1 + multa)
    print(f"Sua fatura com {dias_atraso} dias de atraso e multa é R$ {fatura_com_multa:.2f}")
    fatura = fatura_com_multa
forma_pagamento = input("Escolha a forma de pagamento: 'pix' ou 'boleto': ").lower()
if forma_pagamento == 'pix':
    print(f"Para pagamento via Pix, o valor é R$ {fatura:.2f}. Use a chave Pix: pix@exemplo.com")
elif forma_pagamento == 'boleto':
    print(f"Para pagamento via boleto, o valor é R$ {fatura:.2f}. O boleto será gerado e enviado para o seu e-mail.")
else:
    print("Forma de pagamento inválida. Por favor, escolha 'pix' ou 'boleto'.")
