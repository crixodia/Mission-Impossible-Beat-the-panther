coordenadas = [(2, 3), (-1, 5), (4, -2)]



def sumar_coordenadas(coordenadas):
    x = 0
    y = 0
    for coordenada in coordenadas:
        x += coordenada[0]
        y += coordenada[1]
    return x, y


if __name__ == "__main__":
    print(sumar_coordenadas(coordenadas))
