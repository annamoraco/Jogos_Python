print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

numero_secreto = 45

chute = int(input("Digite um número: "))

print("Você digitou:",chute)

if numero_secreto == chute:
    print("Você acertou!")
else:
    print("Você errou.")