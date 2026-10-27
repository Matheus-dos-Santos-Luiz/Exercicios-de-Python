peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura * 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print('SEU FRANGOOOO')
elif imc >= 18.5 and imc < 25:
    print("Tá no shape")
elif imc > 25 and imc < 35:
    print('Projeto BITELO')
else:
    print('Cê vai MORRER antes do Natal. ')