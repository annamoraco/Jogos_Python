import random


def cabecalho():
    print("\n***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************\n")


def sorteia_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    numero_palavras = int(arquivo.readline())
    linha_palavra = random.randrange(1, numero_palavras + 1)
    index = 1
    for linha in arquivo:
        if index == linha_palavra:
            palavra_secreta = linha.strip().upper()
            break
        index += 1

    arquivo.close()
    return palavra_secreta


def analisa_chute(chute, letras_erradas, palavra_secreta, letras_certas):
    if chute in letras_erradas:
        return letras_certas
    elif chute not in palavra_secreta:
        letras_erradas.append(chute)
    else:
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_certas[index] = chute
            index += 1
    print("\n", letras_certas, "\n")
    return letras_certas


def encerramento_jogo(acertou):
    if acertou:
        print("\nVocê ganhou!!!")
    else:
        print("\nVocê perdeu.")

    print("Fim de Jogo")


def recebe_chute():
    return input("Digite uma letra: ").strip().upper()


def jogar():

    cabecalho()

    palavra_secreta = sorteia_palavra_secreta()

    letras_certas = ["_" for letras in palavra_secreta]
    print(letras_certas, "\n")

    letras_erradas = []
    tentativas = 6
    acertou = False
    enforcou = False

    while (not enforcou and not acertou):

        chute = recebe_chute()

        analisa_chute(chute, letras_erradas, palavra_secreta, letras_certas)

        acertou = "_" not in letras_certas
        enforcou = len(letras_erradas) >= tentativas

    encerramento_jogo(acertou)


if (__name__ == "__main__"):
    jogar()
