""" El bucle while se utiliza para repetir un bloque de código mientras
una condición específica sea verdadera. Es ideal para situaciones en las
que no sabes de antemano cuántas veces necesitas repetir el bloque de
código y la repetición depende de una condición que puede cambiar en
cada iteración. """

# while condición:
    # código a ejecutar mientras la condición sea verdadera
    
    
contador = 1
while contador < 5:
    print(contador)
    contador += 1
    #print(contador) si se activa asi primero suma luego imprime.
"""imprime la variable contador hasta que sea 5 (condicion), comensando
por el valor de la variable en este caso contador = 1."""
""" mientras contador menor que 5: imprime 1 (valor de variable) una vez impreso suma 1
hasta que alcanse 5"""

# usando brake and continue
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break  # Salir del bucle cuando contador sea 5

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Saltar el resto del código en la iteración actual si contador es par
    print(contador)

#Usos comunes:
#while True:
    
import time

# listo = False
# while not listo:    # mientras nosea listo 
#     print("Esperando...")
#     time.sleep(1)   # Detine por segundos una vez imprima esperando y luego continua.
   #listo = verificar_si_listo()  # Supongamos que esta función verifica una condición

# Para uso de usuario es bueno.
while True:
    entrada = input("Ingresa un número positivo: ")
    if entrada.isdigit() and int(entrada) > 0: # para que siempre sea numeros y positivos
        print("Gracias!")
        break
    else:
        print("Entrada no válida, intenta de nuevo.")
