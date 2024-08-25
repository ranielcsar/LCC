class Quadrado:
    def __init__(self, tamanho_lado: int) -> None:
        self.__tamanho_lado = tamanho_lado

    def mudar_tamanho_lado(self, novo_valor: int) -> None:
        print(f"Tamanho do lado atualizado para {novo_valor}")
        self.__tamanho_lado = novo_valor

    def pegar_tamanho_lado(self) -> int:
        return self.__tamanho_lado
    
    def calcular_area(self) -> int:
        return pow(self.__tamanho_lado, 2)

    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre o Quadrado]\nTamanho do lado: {self.__tamanho_lado}\nÁrea: {self.calcular_area()}\n"
        text += "--------------------------------------------------"
        return text
