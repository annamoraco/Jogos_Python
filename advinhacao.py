print("********************************")
print("Bem vindo ao jogo da advinhação!")
print("********************************")

numero_secreto = 45
total_tentativas = 5
rodada = 1

while rodada <= total_tentativas :

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

    rodada = rodada + 1

print("Fim de jogo")