# contador = int(input("me de um numero pra repetir"))
# for i in range(0,contador,2):
#     print(i)

# palavra= input("Fale uma palavra: ")
# for indice in range(len(palavra)):
#     caracter = palavra[indice]
#     print(f"indice {indice}: caracter {caracter}")
palavra = input("me de uma palavra")
vogais = ["a","e","i","o","u"]
contador = 1
quantidade_de_vogais= 0
for letra in palavra:
        if letra in vogais:
            print(f"{contador}:{letra}")
            contador +=1
            quantidade_de_vogais +=1
print(f"a soma de quantidade de vogais e de {quantidade_de_vogais}")