notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
media = 0

while i < len(notas):
    notas[i] = float(input("Digite um numero: "))
    media += notas[i]
    i += 1
media = media / len(notas)

print(f"a media dos alunos foi {media}")