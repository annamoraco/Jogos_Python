print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

numero_secreto = 45
total_tentativas = 5

for rodada in range(1,total_tentativas + 1) :

    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um número: "))
    print("Você digitou:",chute)

    acertou = chute == numero_secreto

    if (acertou):
        print("Parabéns, você ganhou!")
        break
    elif (chute > numero_secreto):
        print("Você errou. O número secreto é menor.")
    else:
        print("Você errou. O número secreto é maior.")

print("Fim de jogo")
range()