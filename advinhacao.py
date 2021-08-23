print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

numero_secreto = 45

chute = int(input("Digite um número: "))

print("Você digitou:",chute)

acertou = chute == numero_secreto

if (acertou):
    print("Você acertou!")
elif (chute > numero_secreto):
    print("Você errou. O número secreto é menor.")
else:
    print("Você errou. O número secreto é maior.")

print("Fim de jogo")