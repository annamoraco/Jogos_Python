import random

def jogar():

    print("\n***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************\n")

    arquivo = open("palavras.txt","r")
    numero_palavras = int(arquivo.readline())
    linha_palavra = random.randrange(1, numero_palavras+1)
    index = 1
    for linha in arquivo:
        if index == linha_palavra:
            palavra_secreta = linha.strip().upper()
            break
        index += 1

    arquivo.close()

    #palavra_secreta = "banana".upper()
    letras_certas = ["_" for letras in palavra_secreta]

    print(letras_certas,"\n")

    letras_erradas = []
    tentativas = 6
    acertou = False
    enforcou = False

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ").strip().upper()

        if chute in letras_erradas:
            continue
        elif chute not in palavra_secreta :
            letras_erradas.append(chute)
        else:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas[index] = chute
                index += 1
        print("\n",letras_certas,"\n")

        acertou = "_" not in letras_certas
        enforcou = len(letras_erradas) >= tentativas

    if acertou:
        print("\nVocê ganhou!!!")
    elif enforcou:
        print("\nVocê perdeu.")

    print("Fim de Jogo")

if(__name__=="__main__"):
    jogar()