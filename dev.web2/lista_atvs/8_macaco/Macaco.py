class Macaco:
    def __init__(self, nome: str, bucho: list[str]) -> None:
        self.__nome = nome
        self.__bucho = bucho

    def comer(self, comida: str) -> None:
        print(f"o macaco {self.__nome} comeu {comida}")
        self.__bucho.append(comida)

    def ver_bucho(self) -> str:
        text = ''
        for comida in self.__bucho:
            text += f"{comida}, "
        
        print(f"comidas no bucho: [{text[:-2]}]")
        return f"[{text[:-2]}]"

    def digerir(self) -> None:
        print("toda comida foi digerida!")
        self.__bucho = []

    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre o Macaco]\nNome: {self.__nome}\nBucho: {self.ver_bucho()}\n"
        text += "--------------------------------------------------"
        return text