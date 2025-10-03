matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def exibir(matriz):
    print("  1 2 3")
    for linha in range(3):
        print(linha + 1, end = ' ')  
        for coluna in range(3):
            print(matriz[linha][coluna], end=' ')
        print()

matriz2 = [['x' for _ in range(3)] for _ in range (3)]

exibir(matriz2)