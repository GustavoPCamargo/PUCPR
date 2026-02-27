idade = [0, 0, 0, 0, 0]
soma = 0
media = 0

for i in range (0, 5):
    idade[i] = int(input("Digite uma idade: "))
    soma += idade[i]
media = soma / len(idade)
print(f"a media das idades é {media}")