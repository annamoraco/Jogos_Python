import random

print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

nivel = 0

while (nivel < 1 or nivel > 3):
    print("Qual o nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input())

    if nivel == 1:
        total_tentativas = 50
    elif nivel == 2:
        total_tentativas = 25
    elif nivel == 3:
        total_tentativas = 10

numero_secreto = random.randrange(0, 101)
pontos = 1000

for rodada in range(1,total_tentativas + 1) :

    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um número entre 0 e 100: "))

    while (chute < 0 or chute > 100) :
        chute = int(input("Valor inválido. Você deve digitar um número entre 0 e 100: "))

    acertou = chute == numero_secreto

    if (acertou):
        print("Parabéns, você ganhou!")
        print(f"Você fez {pontos} pontos")
        break
    else:
        if (chute > numero_secreto):
            print("Você errou. O número secreto é menor.")
        else:
            print("Você errou. O número secreto é maior.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo")