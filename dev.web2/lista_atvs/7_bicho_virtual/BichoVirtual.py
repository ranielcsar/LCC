class BichoVirtual:
    def __init__(self, nome: str, fome: float, saude: float, idade: int):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def alterar_nome(self, nome: str) -> None:
        self.__nome = nome

    def alterar_fome(self, fome: float) -> None:
        self.__fome = fome

    def alterar_saude(self, saude: float) -> None:
        self.__saude = saude

    def alterar_idade(self, idade: int) -> None:
        self.__idade = idade

    def checar_humor(self) -> str:
        if (self.__fome <= 60 & self.__saude <= 60):
            return "Está mal humorado"

        if (self.__fome <= 30 & self.__saude <= 30):
            return "Não está nada bem..."
        
        return "Está de bom humor"
        
    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre o Bicho Virtual]\nNome: {self.__nome}\nFome: {self.__fome:.2f}%\nSaúde: {self.__saude:.2f}%\nIdade: {self.__idade}\n{self.checar_humor()}\n"
        text += "--------------------------------------------------"
        return text

        