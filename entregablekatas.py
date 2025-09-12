
""" 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena.
Los espacios no deben ser considerados. """

def posiciones_letras(cadena):
    
    posiciones = {}
    
    
    for indice, letra in enumerate(cadena):
         if 'a' <= letra <= 'z':
            
            if letra in posiciones:
                posiciones[letra].append(indice)
            else:
                posiciones[letra] = [indice]
                
    return posiciones

resultado = posiciones_letras("hola mundo")
print(resultado)



"""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map() """

lista_numeros = [1, 2, 20, 54, 67, 222]
def lista_numeros_dobles(lista_numeros):
    return (lista_numeros * 2)
lista_numeros_dobles = map(lista_numeros_dobles, lista_numeros)
resultado = list(lista_numeros_dobles)
print(resultado)



""" 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

"""lista_palabras = [camisa, pantalón, zapatos, corbata, americana]"""

""" 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""

lista_numeros = [1, 2, 20, 54, 67, 222]
lista_numeros_dobles = [2, 4, 40, 108, 134, 444]


def resta_listas(lista_numeros_dobles, lista_numeros):

# o def diferencia(x, y):
        # return x - y
 return list(map(lambda x, y: x - y, lista_numeros, lista_numeros_dobles))
    
    # Usar map para aplicar la función de diferencia a cada par de elementos
    # return list(map(diferencia, lista_numeros, lista_numeros_dobles))

# Ejemplo de uso
 
resultado = resta_listas(lista_numeros, lista_numeros_dobles)
print(resultado)

""" 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""

lista_notas = [3, 6, 8, 3]
nota_aprobado =5 
def nota_final (lista_notas, nota_aprobado):
    
    if np.mean(lista_notas) == nota_aprobado:
        return "aprobado"
    else:
        return "suspenso"
    
resultado = nota_final(lista_notas, nota_aprobado)
print(resultado)

""" 6. Escribe una función que calcule el factorial de un número de manera recursiva. """

n=3
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

         #3 * 2 * 1
print(factorial(n))  


""" 7. Genera una función que convierta una lista de tuplas a una lista de strings. Funcion map()"""
def convert_tuples_to_strings(lista_tupla):
    return list(map(str, lista_tupla))


lista_tupla = [(1, 2), (3, 4), (5, 6)]
result = convert_tuples_to_strings(lista_tupla)
print(result)


""" 8.Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.
 """
# Pedir al usuario que ingrese dos números
def dividir_numeros():
  try:  
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    result = num1 / num2
    print("El resultado de la división es:", result)
  except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
  except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")
    

dividir_numeros()

"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""

lista_mascotas = ["gato", "tigre", "perro", "oso", "leon", "hamster", "serpiente pitón"]
lista_mascotas_prohibidas = ["mapache", "tigre",
"serpiente pitón", "cocodrilo", "oso"]


def filtrar_mascotas(lista_filtrada):
  return lista_filtrada not in lista_mascotas_prohibidas

lista_filtrada = filter(filtrar_mascotas,lista_mascotas)


result = list(lista_filtrada)
print(result)



""" 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente """

numeros= []

def media (numeros):

    if len(numeros) == 0: 
        return(f"La lista está vacía, no es posible calcular la media")  
        
    return sum(numeros) / len(numeros)


media = media(numeros)
print(media) 


""" 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente."""

def conocer_edad(edad):
    try:
        edad = float(input("Ingrese su edad"))
        if edad <= 0 or edad > 120:
            print(f"Debe añadir un número válido")
        else:
            print(f"Usted tiene {int(edad)} años")

    except ValueError:
        print("Error: Por favor, ingrese solo valores numéricos.")

conocer_edad(edad)


"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
"""
frase = "Hola, hoy es sabado"

def longitud (frase):
    palabras = frase.split()
    longitud = map(len, palabras)
    return (longitud)



resultado = list(longitud(frase))
print(resultado)



""" 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas ."""

def generar_tuplas_caracteres(caracteres):
    
    lista_tuplas = [(car.upper(), car.lower()) for car in caracteres]
    return lista_tuplas


caracteres = 'MaRiIIAa'
resultado = set(generar_tuplas_caracteres(caracteres))
print(resultado) 


""" 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""

def return_palabras(lista_palabras, letra):
    lista_palabras = filter(lambda palabras: palabras.startswith(letra), lista_palabras)
    return list(lista_palabras)

lista_palabras =["María", "Marta", "Carmen", "Almudena", "Mercedes"]
letra = "M"
result = return_palabras(lista_palabras, letra)
print(result)


""" 15. Crea una función lambda que sume 3 a cada número de una lista dada."""
def sumar (lista_numeros):
    lista_numeros = map(lambda numero: numero +3, lista)
    return lista_numeros

lista = [1, 2, 3, 4]
result = list( sumar (lista_numeros))
print(result)


"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""

def palabras_largas (texto, numero):
    palabras =texto.split()
    lista_palabras_largas = filter(lambda palabras: len(palabras) > numero, palabras)
    return list (lista_palabras_largas)

texto = "hola , feliz lunes a todos"
numero = 4
result = palabras_largas(texto, numero)
print (result)

"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""

from functools import reduce
def num_lista (num1, num2 ):
    
    return num1 + num2

lista_digitos = [3, 54, 1]
result = reduce(num_lista,  map(str,lista_digitos))
print(result)


""" 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""
estudiantes = []
def agregar_estudiante(nombre, edad, calificacion):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion
    }
    
    
    estudiantes.append(estudiante)

# Agregar algunos estudiantes
agregar_estudiante('Almudena', 20, 85.20)
agregar_estudiante('María', 22, 90.10)
agregar_estudiante('Marta', 21, 78)
agregar_estudiante('Mercedes', 19, 92)

estudiantes_nota_alta = list(filter(lambda estudiante: estudiante["calificacion"]>=90, estudiantes))
 

print(estudiantes_nota_alta)


""" 19. Crea una función lambda que filtre los números impares de una lista dada. """


def numeros_pares(lista_numeros):

    lista_numeros_pares = filter(lambda numero: numero % 2 ==0, lista_numeros)
    return lista_numeros_pares

lista_numeros = [3,6, 9 , 22, 44]
result = list(numeros_pares(lista_numeros))
print(result)



""" Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
filter() """



lista_datos = ["maria", 30, "carmen", 28, "lucia", 22] 
lista_int = list(filter(lambda dato: type(dato)==int, lista_datos))


print (lista_int)


""" 21. Crea una función que calcule el cubo de un número dado mediante una función lambda """

cubo = lambda x: x**3
resultado =cubo(2)

print(resultado)

"""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ."""

from functools import reduce


lista_digitos = [3, 54, 1, 2] 

suma_total = reduce(lambda x,y: x+y, lista_digitos)
print(suma_total)



"""23. Concatena una lista de palabras.Usa la función reduce()"""

lista_palabras = ["hola" "que" "tal" "?"]

concat_palabras = reduce(lambda x,y: x+y, lista_palabras)
print(concat_palabras)


"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
"""
lista_digitos = [54, 3, 1, 2] 

suma_total = reduce(lambda x,y: x-y, lista_digitos)
print(suma_total)


""" 25. Crea una función que cuente el número de caracteres en una cadena de texto dada. """
def numero_caracteres(cadena_texto):
    return len(cadena_texto)


cadena_texto = "hola, soy maria"
result = numero_caracteres(cadena_texto)
print(result)

""" 26. Crea una función lambda que calcule el resto de la división entre dos números dados."""
dividendo_numero = lambda x,y: x % y


x= 4
y=2

resultado = dividendo_numero(x,y)
print(resultado)

""" 27. Crea una función que calcule el promedio de una lista de números."""


def promedio(lista_numeros):
    numero_promedio = (sum(lista_numeros))// len(lista_numeros)
    return numero_promedio
lista_numeros = [2,4,6, 10]
result = promedio(lista_numeros)
print(result)


""" 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""
def elemento_duplicado(lista_duplicados):
    num_duplicado =[]
    for elemento in lista_duplicados:
     
     if elemento in num_duplicado :
         return elemento 
     num_duplicado.append(elemento)
    return None

lista_duplicados = [1,  2,2, 4]
primer_duplicado = elemento_duplicado(lista_duplicados)
print(primer_duplicado)



""" 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro. """

def enmascarar_variable (variable):
    
   nueva_variable= variable.replace(variable[:-4], "#"*4)
   return nueva_variable

variable = "12345678911"

lista_enmascarada = enmascarar_variable (variable)
print(lista_enmascarada)


""" 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""


def palabras_anagramas(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        return f"Las palabras son anagramas"
    else:
        return f"Las palabras no son anagramas"

palabra1= "lorca"
palabra2="calor"

resultado = palabras_anagramas(palabra1, palabra2)
print(resultado)


"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""

def solicitar_lista_nombres_buscar():
    lista_nombres = []
    while nombres := input("Ingresa una lista de nombres"):
        if nombres == "":
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


"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí.
"""
empleados = { "María Rosa": "Economista",
             "Carmen Luna": "Arquitecta",
             "Claudia Aparicio": "Ingeniera",
             "Belen Rodriguez": "Publicista"
}

empleado = "Carmen Luna"

def empleado_en_listado (empleados):
    if empleado in empleados:
        return f"El empleado {empleado} trabaja como {empleados[empleado]}."
    else:
        return f"el empleado '{empleado}' no trabajada en esta empresa."
    

resultado = empleado_en_listado (empleados)
print(resultado)


""" 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas. """
lista_numeros = [1, 2, 20, 54, 67, 222]
lista_numeros_dobles = [2, 4, 40, 108, 134, 444]


lista_sumada = list(map(lambda x, y: x + y, lista_numeros, lista_numeros_dobles))
    

print(lista_sumada)


""" 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol."""

 
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1 #Aumentar
        print (f"El tronco ha crecido a {self.tronco} unidades.")

    def nueva_rama(self):
        self.ramas.append(1) #Agregar
        print(f"Se ha añadido una nueva rama de longitud 1. El total de ramas es {len(self.ramas)}.")

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] +=1 #aumentar cada rama agregada
        print(f"Todas las ramas han crecido a un total de {self.ramas[i]} unidades" )
    
    def quitar_rama(self, posicion):
        if 0<=posicion< len(self.ramas):
            eliminar_rama= self.ramas.pop(posicion)
            print(f"La rama en la posición {posicion} (longitud {eliminar_rama}) ha sido quitada.")
        else:
            print(f"Posición inválida. No se puede quitar la rama.")
    def info_arbol(self):
        info = f"El tronco tiene {self.tronco} unidades de longuitud, y las ramas son {len(self.ramas)}."
        return info

"""1. Crear un árbol."""
arbol = Arbol()
print(arbol.info_arbol())

print(f"____________________")

"""2. Hacer crecer el tronco del árbol una unidad."""
arbol.crecer_tronco()
print(f"____________________")
"""3. Añadir una nueva rama al árbol."""
arbol.nueva_rama()
print(f"____________________")
"""4. Hacer crecer todas las ramas del árbol una unidad."""

arbol.crecer_ramas()
print(f"____________________")
"""5. Añadir dos nuevas ramas al árbol."""
arbol.nueva_rama()
arbol.nueva_rama()
print(f"____________________")

"""6. Retirar la rama situada en la posición 2."""
arbol.quitar_rama(2)
print(f"____________________")

""" 7. Obtener información sobre el árbol."""
print(arbol.info_arbol())
print(f"____________________")



""" 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo."""

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
     
        if cantidad < otro_usuario.saldo: 
            
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
       return f" El cliente {self.nombre} tiene un saldo de {self.saldo} €. { "Tiene cuenta corriente" if self.cuenta == True 
                                                                              else "No tiene cuenta corriente"}"
    

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


""" 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto ."""

def procesar_texto(texto):
    opcion = input()
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto)
    elif opcion == "eliminar":
        
        return eliminar_palabra(texto)
        
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
    
def reemplazar_palabras(texto):
      palabras = texto.split() 
      nuevo_texto = texto.replace(palabra_original, palabra_nueva)
      return nuevo_texto

def eliminar_palabra(texto):
    palabras = texto.split() 
    palabra_eliminada =  [p for p in palabras if p not in eliminar]
    return ' '.join(palabra_eliminada)

texto = "Hoy es Martes y son las 10 am"
eliminar = "am"
palabra_original = "am"
palabra_nueva = "pm"
result= procesar_texto(texto)
print (result)










"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario. """
def horas_dia():
    try:
        hora = float(input(f"¿qué hora es?"))
        if 7<hora<15:
            return f"Son las {hora} horas y es de día."
        elif 15<hora<20: 
            return f"Son las {hora} horas y es por la tarde."
        else:
            return f"Son las {hora} y es de noche."
    
    except ValueError:
        print("Error: Por favor, ingrese solo valores numéricos.")
        
resultado= horas_dia() 
print(resultado)
    
""" 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica."""

def calificacion():
    try:
        nota = float(input(f"¿qué calificación tienes?"))
        if 0<=nota<=69:
            return f"Tu nota es {nota}, y es 'insuficiente'."
        elif 69<nota<=79: 
            return f"Tu nota es {nota}, y es 'bien'."
        elif 79<nota<=89: 
            return f"Tu nota es {nota}, y es 'muy bien'."
        elif 89<nota<=100:
            return f"Tu nota es {nota}, y es 'excelente'."
    
    except ValueError:
        print("Error: Por favor, ingrese solo valores numéricos.")
        
resultado= calificacion() 
print(resultado)



""" 40.Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o 
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""

def area_figura(figura, datos):
    
    if figura == "triangulo":
        base, altura = datos
        area = (base * altura) / 2
        return area
    elif figura == "circulo":
        radio = datos
        area = 3.14 * (radio ** 2)
        return area
    elif figura == "rectangulo":
        base, altura = datos
        area= base * altura
        return area
    else:
        raise ValueError ("La figura introducida no es correcta")
    
 
 
result= area_figura( "circulo", 4)
print (f"El área es: {result}")



"""41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. """


precio_original = float(input(f"Ingresa el precio original del artículo"))
print (f"El precio original del artículo es de {precio_original} €")


cupon_descuento = (input(f"¿Tienes cupón de descuento? Responde si o no")).lower()
print(f"Tienes cupón descuento: {cupon_descuento}")




def precio_compra(precio_original):
    
    if cupon_descuento == "si":
        descuento = float(input(f"Ingrese el valor del cupón de descuento"))

        print(f"Tu descuento es de {descuento}")
        
        if descuento >0 :
    
            precio_original -= descuento
            return precio_original
        else:
            print(f"No tienes descuento a aplicar porque el valor es 0")
            return precio_original
    else:
        
        print(f"No tienes descuento a aplicar") 
        return precio_original

        

result= precio_compra(precio_original)
print(f"El precio final de la compra es de {result} €")