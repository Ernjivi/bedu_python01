#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crear e imprimir una lista de tres personas donde cada persona incluya
nombre, apellido paterno y edad, además cada persona deberá de ser una
instancia de la clase Persona(). Se debe hacer uso de las funciones
obtener_personas() e imprimir_personas().
"""

# Se defina la clase Persona() con atributos: nombre, apellido paterno y
# edad.
class Persona:
    """ Se define el objeto Persona """
    def __init__(self, nombre, a_paterno, edad):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.edad = edad


def obtener_personas():
    """ Crea y regresa una lista de objetos de tipo Persona() """

    # Se crea la lista de objetos Persona()
    personas = [
        Persona("Hugo", "Smith", 8),
        Persona("Paco", "Lorenz", 28),
        Persona("Luis", "Tesla", 38)
    ]

    return personas

def imprimir_personas(lista):
    """
    Imprime la lista de personas en lista donde cada elemento debe ser
    de tipo Persona()
    """
    an = 15  # Ancho de columna nombre
    aa = 16  # Ancho de columna a_paterno
    ae = 4   # Ancho de columna edad
    at = an + aa + ae + 2  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}}".format("Nombre", an, "Apellido", aa,
        "Edad", ae))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de personas
    for persona in lista:
        print("{:{}} {:{}} {:{}}".format(persona.nombre, an,
            persona.a_paterno, aa, persona.edad, ae))
    # Imprime otro separador
    print("-" * at)

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Persona.
lista_personas = obtener_personas()

# Se hace uso de una función cuya única tarea es imprimir la lista de
# personas
imprimir_personas(lista_personas)

