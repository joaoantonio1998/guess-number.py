import random

print("Seja bem vindo ao guess number!")
numero=int(input("Digite o numero teto do desafio: "))

random_number = random.randint(0, numero)

chances = 0

while True:
    resposta = int(input("Advinhe o numero: "))
    chances = chances + 1
    if resposta == random_number:
        print("Acertou!")
        break

    elif resposta > random_number:
        print("Acima do numero!")
    else:
        print("Abaixo do numero!")

print("-------------------")
print(f"chutes : {chances}")