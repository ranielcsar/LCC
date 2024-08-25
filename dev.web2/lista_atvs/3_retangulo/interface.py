from Retangulo import Retangulo
from mdc import maior_divisor_comum

print("[Informe as medidas do local]")
base = int(input("Tamanho da base em metros: "))
altura = int(input("Tamanho da altura em metros: "))
print("\n")

def format_number(number: int) -> str:
    return f"{number:,}".replace(",", ".")

def print_retangulo_infos(retangulo: Retangulo):
    tamanho_piso = maior_divisor_comum(retangulo.pegar_tamanho_base(), retangulo.pegar_tamanho_altura())
    total_pisos = int(retangulo.calcular_area() / tamanho_piso)
    print(retangulo)
    print(f"Tamanho do piso: {tamanho_piso}m x {tamanho_piso}m")
    print(f"Total de pisos quadrados necessários para o local: {format_number(total_pisos)}" )
    print(f"Perímetro do local: {format_number(retangulo.calcular_perimetro())}m" )
    print(f"Área do local: {format_number(retangulo.calcular_area())}m²" )
    print("--------------------------------------------------")

retangulo = Retangulo(base, altura)
print_retangulo_infos(retangulo)
print("\n")
retangulo.mudar_tamanho_base(1460)
retangulo.mudar_tamanho_altura(620)
print("\n")
print_retangulo_infos(retangulo)