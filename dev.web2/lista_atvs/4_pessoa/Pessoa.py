class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self) -> None:
        self.__idade += 1

        if (self.__idade < 21):
            self.__altura += 0.05
            print(f"Parabéns, {self.__nome}! Você ficou um ano mais velho! Agora tem {self.__idade} anos, cresceu 0,5cm e mede {self.__altura}m!")
            return
        print(f"Parabéns, {self.__nome}! Você ficou um ano mais velho e agora tem {self.__idade} anos!")

    def engordar(self, kg: float) -> None:
        print(f"Você engordou {kg}kg, {self.__nome}")
        self.__peso += kg

    def emagrecer(self, kg: float) -> None:
        print(f"Você emagreceu {kg}kg, {self.__nome}")
        self.__peso -= kg

    def crescer(self, cm: float) -> None:
        print(f"Você cresceu {cm}cm, {self.__nome}!")
        self.__altura += cm / 100

    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre a Pessoa]\nNome: {self.__nome}\nIdade: {self.__idade}\nPeso: {self.__peso}\nAltura: {self.__altura}m\n"
        text += "--------------------------------------------------"
        return text