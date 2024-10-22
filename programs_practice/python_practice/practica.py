def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

total = sumar(2, 5)
mensaje_saludo = saludar("Jose")
print(f"Puntos: {total}, {mensaje_saludo}")  # Imprime: Puntos: 7, Hola, Jose

min = 8
max = 10
print(f"{88}% of user are {min} and {max}")

print(bool("abc"))