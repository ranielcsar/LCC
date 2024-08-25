class ContaCorrente:
    def __init__(self, numero_conta: str, nome_correntista: str, saldo = 0.0):
        self.__numero_conta = numero_conta
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo

    def __format_number(self, number: float) -> str:
        return f"{number:,}".replace(".", ",")

    def alterar_nome(self, novo_nome: str) -> None:
        self.__nome_correntista = novo_nome
        print(f"Nome da conta atualizado! Novo nome: {novo_nome}")

    def deposito(self, valor: float):
        self.__saldo += valor
        print(f"Depósito no valor de R$ {self.__format_number(valor)} realizado! Novo saldo da conta: R$ {self.__format_number(self.__saldo)}")

    def saque(self, valor: float) -> None:
        if (self.__saldo <= valor):
            print("Saldo indisponível")
            return
        self.__saldo -= valor        
        print(f"Saque no valor de R$ {self.__format_number(valor)} realizado! Novo saldo da conta: R$ {self.__format_number(self.__saldo)}")
        
    def __str__(self) -> str:
        text = "--------------------------------------------------\n"
        text += f"[Informações sobre a Conta]\nNome do correntista: {self.__nome_correntista}\nNº da conta: {self.__numero_conta}\nSaldo: R$ {self.__format_number(self.__saldo)}\n"
        text += "--------------------------------------------------"
        return text

        