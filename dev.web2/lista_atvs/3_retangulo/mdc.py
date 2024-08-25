# algoritmo de euclides
def maior_divisor_comum(dividendo: int, divisor: int) -> int:
    if divisor == 0:
        return dividendo
             
    resto = dividendo % divisor
    return maior_divisor_comum(divisor, resto)