class Retangulo:
    def __init__(self, base: int, altura: int) -> None:
        self.__base = base
        self.__altura = altura

    def mudar_tamanho_base(self, novo_valor: int) -> None:
        print(f"Tamanho da base atualizado para {novo_valor}m")
        self.__base = novo_valor

    def mudar_tamanho_altura(self, novo_valor: int) -> None:
        print(f"Tamanho da altura atualizado para {novo_valor}m")
        self.__altura = novo_valor

    def pegar_tamanho_base(self) -> int:
        return self.__base
    
    def pegar_tamanho_altura(self) -> int:
        return self.__altura
    
    def calcular_area(self) -> int:
        return self.__base * self.__altura
    
    def calcular_perimetro(self) -> int:
        return 2 * (self.__base + self.__altura)

    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre o Retângulo]\nBase: {self.__base}m\nAltura: {self.__altura}m\n"
        text += "--------------------------------------------------"
        return text
