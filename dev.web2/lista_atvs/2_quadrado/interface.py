from Quadrado import Quadrado

quadrado = Quadrado(4)
print(quadrado)
quadrado.mudar_tamanho_lado(6)
quadrado.pegar_tamanho_lado()
print(f"Área do quadrado: {quadrado.calcular_area()}")