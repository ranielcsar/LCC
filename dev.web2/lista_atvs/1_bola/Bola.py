class Bola:
    def __init__(self, cor: str, circunferencia: int, material: str) -> None:
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def troca_cor(self, nova_cor: str) -> None:
        print(f"A cor da bola {self.__cor} foi trocada por {nova_cor}")
        self.__cor = nova_cor

    def mostra_cor(self) -> None:
        print(f"Cor da bola: {self.__cor}")

    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre a Bola]\nCor: {self.__cor}\nCircunferência: {self.__circunferencia}\nMaterial: {self.__material}\n"
        text += "--------------------------------------------------"
        return text
