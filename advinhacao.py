import random

print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

numero_secreto = random.randrange(0, 101)
total_tentativas = 15

for rodada in range(1,total_tentativas + 1) :

    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um número entre 0 e 100: "))

    while (chute < 0 or chute > 100) :
        chute = int(input("Valor inválido. Você deve digitar um número entre 0 e 100: "))

    acertou = chute == numero_secreto

    if (acertou):
        print("Parabéns, você ganhou!")
        break
    elif (chute > numero_secreto):
        print("Você errou. O número secreto é menor.")
    else:
        print("Você errou. O número secreto é maior.")

print("Fim de jogo")