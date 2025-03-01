import random

# Parámetros
NUM_COUNT = 10_000_000
RANGE_MIN = -50_000_000
RANGE_MAX = 50_000_000
FILE_NAME = "numeros.txt"

# Generar números aleatorios y guardarlos en un archivo
with open(FILE_NAME, "w") as file:
    numeros = [str(random.randint(RANGE_MIN, RANGE_MAX)) for _ in range(NUM_COUNT)]
    file.write("\n".join(numeros))

print(f"Se generaron {NUM_COUNT} números y se guardaron en {FILE_NAME}")

# Cargar los números en un conjunto para búsquedas rápidas
with open(FILE_NAME, "r") as file:
    numeros_set = set(map(int, file.readlines()))

def buscar_numero(n):
    """Busca un número en la estructura de datos."""
    return n in numeros_set

# Prueba de búsqueda
numero_a_buscar = random.randint(RANGE_MIN, RANGE_MAX)
if buscar_numero(numero_a_buscar):
    print(f"El número {numero_a_buscar} está en el archivo.")
else:
    print(f"El número {numero_a_buscar} no está en el archivo.")