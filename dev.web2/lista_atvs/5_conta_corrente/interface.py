from ContaCorrente import ContaCorrente

conta = ContaCorrente("1650 1680 6868 6898", "noob", 120.65)
print(conta)
conta.alterar_nome("Noobin")
conta.deposito(20.5)
conta.saque(120.65)
print(conta)