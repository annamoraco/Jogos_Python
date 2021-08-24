def jogar():

    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    letras_certas = []
    palavra_secreta = "banana".upper()
    for letras in palavra_secreta:
        letras_certas.append("_")

    print(letras_certas)

    acertou = False
    enforcou = False

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ").strip().upper()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(f"Encontrei a letra {letra} na posiçào {index}")
                letras_certas[index] = chute
            index = index + 1
        print(letras_certas)

        if "_" not in letras_certas :
            acertou = True
            print("Você ganhou!!!")

    print("Fim de Jogo")

if(__name__=="__main__"):
    jogar()