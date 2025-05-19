# Solicita ao usuario que digite sua idade
idade = int(input("Digite sua idade: "))

# Verifica se a idade e maior que 18
if idade > 18:
    print("Voce e maior de idade")

# Verifica se a idade e exatamente 18
elif idade == 18:
    print("Voce tem exatamente 18 anos")

# Se nao for maior e nem exatamente 18, entao e menor de idade
else:
    print("Voce e menor de idade")
