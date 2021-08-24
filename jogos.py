import forca
import adivinhacao

print("************************")
print("****Escolha deu Jogo****")
print("************************")

print("(1) Adivinhação   (2) Forca")
jogo = int(input());

if jogo == 1 :
    adivinhacao.jogar()
elif jogo == 2:
    forca.jogar()