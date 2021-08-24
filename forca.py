def jogar():

    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    palavra_secreta = "banana".upper()
    letras_certas = ["_" for letras in palavra_secreta]

    print(letras_certas)

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
        print(letras_certas)

        acertou = "_" not in letras_certas
        enforcou = len(letras_erradas) >= tentativas

    if acertou:
        print("Você ganhou!!!")
    elif enforcou:
        print("Você perdeu.")

    print("Fim de Jogo")

if(__name__=="__main__"):
    jogar()