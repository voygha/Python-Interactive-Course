""" Introducción a diagramas de flujo
Ideas clave:
Los programas por defecto se ejecutan de manera lineal, de arriba a abajo.
Podemos cambiar el flujo de un programa utilizando sentencias de control de flujo.
Los diagramas de flujo son una herramienta visual que nos permite representar el flujo de un programa.
Diagramas de flujo
El flujo de un programa es el orden en el que se ejecutan las instrucciones y, si bien podemos seguir el flujo de un programa leyendo el código, a veces es más fácil visualizarlo. Para esto se utilizan los diagramas de flujo, que son una herramienta visual que nos permite representar el flujo de un programa.

Los diagramas de flujo se componen de bloques que representan instrucciones y flechas que indican el flujo de ejecución. Cada bloque tiene una forma específica que indica el tipo de instrucción que representa. Por ejemplo, un bloque rectangular representa una instrucción, un rombo representa una condición y un óvalo representa el inicio o fin del programa.

Código y diagramas de flujo
Veamos un ejemplo lineal primero.

print("Inicio del programa")
print("Instrucción 1")
print("Instrucción 2")
print("Instrucción 3")

flowchart TD
    A[Inicio del programa] --> B[Instrucción 1]
    B --> C[Instrucción 2]
    C --> D[Instrucción 3]
    D --> E[Fin del programa]
Veamos un ejemplo con una condición.

numero = 10
if numero > 5:
    print("El número es mayor que 5")
flowchart TD
    A[Inicio] --> B(Asignar el texto 'hola' a la variable 'saludo')
    B --> C{¿El saludo es igual a 'hola'?}
    C -->|Sí| D[Mostrar 'Es el saludo correcto']
    D --> E[Fin]
    C -->|No| E[Fin] """


""" Implementa el siguiente código a partir de un diagrama de flujo.


# Escribe tu código aquí
 A[Inicio] --> B(Asignar el texto 'hola' a la variable 'saludo')
    B --> C{¿El saludo es igual a 'hola'?}
    C -->|Sí| D[Mostrar 'Es el saludo correcto']
    D --> E[Fin]
    C -->|No| E[Fin]
# Fin """
