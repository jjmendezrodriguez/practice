"""como usar los loop de for
for variable in iterable:
    código a ejecutar en cada iteración"""

#iterable:

my_list = [1, 2, 3, 4, 5] # puedes editarla a diferencia de la tuple (list)
my_tuple = (1, 2, 3, 4, 5) # no de edita una vez creada (tuple)
my_string = "Hola" # cadena de text (str)
my_diccionary = {'a': 1, 'b': 2, 'c': 3} # 'elemento':valor (dict)
mi_conjunto = {1, 2, 3, 4, 5} # un conjunto de (set)
mi_rango = range(1, 6) # rango (range)


for i in range(1, 6):
    print(i)

num_list = [10, 20, 30, 40, 50]
for elemento in num_list:
    print(elemento)

program = "Python"
for letters in program:
    print(letters)
    
my_diccionary = {'a': 1, 'b': 2, 'c': 3}
for clave in my_diccionary:
    print(clave, my_diccionary[clave])

# Acumulador
suma = 0
for num in [1, 2, 3]:
    suma += num

# Condicionales 
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

# Call funtions
def cuadrado(x):
    return x * x

for num in [1, 2, 3]:
    print(cuadrado(num))

# Modify list
mi_lista = [1, 2, 3]
for i in range(len(mi_lista)):
    mi_lista[i] *= 2

# Built list
cuadrados = [x * x for x in range(1, 6)]

# uso de brake y continue
for num in range(1, 10):
    if num == 5:
        break  # Salir del bucle
    if num % 2 == 0:
        continue  # Saltar a la siguiente iteración
    print(num)
