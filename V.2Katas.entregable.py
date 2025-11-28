
import pandas as pd
import numpy as np

# ejericio 5

lista_notas = [6, 6, 5, 8]
 
def nota_final (lista_notas, nota_aprobado=5):
    
    media = sum(lista_notas) / len(lista_notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
    
resultado = nota_final(lista_notas)
print(resultado)


# ejercicio 10
numeros= []

def media (numeros):

    if len(numeros) == 0: 
        return ValueError("La lista no puede estar vacía")
        
    return sum(numeros) / len(numeros)


media = media(numeros)
print(media) 

#ejericicio 13
def generar_tuplas_caracteres(caracteres):
    
    lista_resultado = []
    lista_usadas =[]
    
    for car in caracteres:
        car = car.lower()
        if car not in lista_usadas:
            lista_resultado.append((car.upper(), car))
            lista_usadas.append(car)
    return lista_resultado 

caracteres = 'MaRiIIAa'
resultado = generar_tuplas_caracteres(caracteres)
print(resultado) 

#ejercicio 15
def sumar (lista_dada):
    for numero in lista_dada:
        return map(lambda numero: numero +3, lista_dada)

lista_dada = [1, 2, 3, 4]

result = list( sumar (lista_dada))
print(result)


#ejericio 18

estudiante = [{"nombre": "Almudena", "edad": 20, "calificacion": 85.20},
    {"nombre": "María", "edad": 22, "calificacion": 90.10},
    {"nombre": "Marta", "edad": 21, "calificacion": 78},
    {"nombre": "Mercedes", "edad": 19, "calificacion": 92}]


estudiantes_nota_alta = list(filter(lambda estudiante: estudiante["calificacion"]>=90, estudiante))
 

print(estudiantes_nota_alta)


#ejericicio 31

def solicitar_lista_nombres_buscar():
    lista_nombres = []
    while True:
    
        nombres = input("Ingresa una lista de nombres, escribe 'fin' para terminar):")
        if nombres.lower() == "fin":
            break
        lista_nombres.append(nombres)


    nombre_buscar = input("ingrese el nombre a buscar:")
    if nombre_buscar in lista_nombres:
        print (f"el nombre que buscas es '{nombre_buscar}' y está en la lista")
    else:
        raise ValueError (f"El nombre que buscas es '{nombre_buscar}' y no está en la lista dada")
    
    return lista_nombres

result = solicitar_lista_nombres_buscar()
print (result)



#ejercicio 36
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta

        
    def retirar_dinero(self, cantidad):


        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en cuenta.")
        self.saldo -= cantidad  # Disminuir el saldo
        print(f"Se ha retirado {cantidad} € de la cuenta y su saldo actual es de {self.saldo}.")


    def transferir_dinero(self, otro_usuario, cantidad):
     
        if cantidad <= otro_usuario.saldo: 
            
            otro_usuario.saldo -=cantidad
            self.saldo += cantidad
            print(f"Se ha transferido desde la cuenta de {otro_usuario.nombre} un total de {cantidad} €")
            print(f"El nuevo saldo del cliente es de {self.saldo} €.")
        else:
            print ("El usuario no tienen suficiente dinero en cuenta para realizar la transferencia.")
    
    def agregar_dinero (self, cantidad): 
       self.saldo += cantidad
       print (f" Se ha agregado a la cuenta {cantidad}€, el cliente {self.nombre} tiene un saldo de {self.saldo}")

    def info_cliente(self):
       return f" El cliente {self.nombre} tiene un saldo de {self.saldo} €." +\
          ("Tiene cuenta corriente" if self.cuenta == True else "No tiene cuenta corriente")
    

    """ Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. """
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco ("Bob", 50, True)

print(usuario1.info_cliente())
print(usuario2.info_cliente())
"""2. Agregar 20 unidades de saldo de "Bob"."""

usuario2.agregar_dinero(20)

""" 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"."""
usuario1.transferir_dinero(usuario2, 80)

""" 4. Retirar 50 unidades de saldo a "Alicia"."""


usuario1.retirar_dinero(50)


#ejercicio 37
def procesar_texto(texto):
    
    opcion = input(f'Elige entre "contar", "reemplazar" o "eliminar"')
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        palabra_original = input (f'Introduce Palabra a reemplazar')
        palabra_nueva = input (f'Introduce la Palabra nueva')
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    
    elif opcion == "eliminar":
        palabra_eliminar = input (f'Introduce la palabra que desa eliminar')
        return eliminar_palabra(texto,palabra_eliminar)
        
    else:
        raise ValueError("La opción no es válida")
    

def contar_palabras(texto):
    palabras = texto.split()
    numero_palabras = {}
    for palabra in palabras: 
        if palabra in numero_palabras:
            numero_palabras[palabra] += 1
        else:
            numero_palabras[palabra] =1
    return numero_palabras
    
def reemplazar_palabras(texto,palabra_original, palabra_nueva):
      palabras = texto.split() 
      nuevo_texto = texto.replace(palabra_original, palabra_nueva)
      return nuevo_texto

def eliminar_palabra(texto, eliminar):
    palabras = texto.split() 
    palabra_eliminada =  [p for p in palabras if p not in eliminar]
    return ' '.join(palabra_eliminada)

texto = "Hoy es Martes y son las 10 am"

result= procesar_texto(texto)
print (result)
