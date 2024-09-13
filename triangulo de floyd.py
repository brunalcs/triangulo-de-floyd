linha = int(input("Digite o número de linhas: "))
num = 1

if linha > 0:
    for c in range (1, linha + 1): # Para cada linha de 1 até linha
        for j in range(c):
            print(num, end=" ")
            num += 1
        print()
else:
    print(f"Você entrou com {linha}, tente de novo na próxima")



