#!/usr/bin/env python
# coding: utf-8

# In[47]:


#MAESTRÍA EN INTELIGENCIA ARTIFICIAL APLICADA
#Pruebas de software y aseguramiento de la calidad
#Dr. Gerardo Padilla Zárate

#Actividad 4.2. Ejercicios de Programación 1
#CARLOS ENRIQUEZ GORGONIO
#A01793102
#20 de febrero de 2024


# In[ ]:


'''Ejercicio 2. Converter
Detalles
Req1. The program shall be invoked from a command line. The program shall receive a file as parameter. The file will contain a list of items (presumable numbers).
Req 2. The program shall convert the numbers to binary and hexadecimal base. The results shall be print on a screen and on a file named ConvertionResults.txt.All computation MUST be calculated using the basic algorithms, not functions or libraries.
Req 3. The program shall include the mechanism to handle invalid data in the file. Errors should be displayed in the console and the execution must continue.
Req 4. The name of the program shall beconvertNumbers.py
Req 5. The minimum format to invoke the program shall be as follows:python convertNumbers.py fileWithData.txt
Req 6. The program shall manage files having from hundreds of items to thousands of items.
Req 7. The program should include at the end of the execution the time elapsed for the execution and calculus of the data. This number shall be included in the results file and on the screen.
Req 8. Be compliant with PEP8
'''


# In[13]:


get_ipython().system('pip install pylint')
get_ipython().system('pip install pylint[spelling]')


# In[5]:


import sys
import time


# In[1]:


#Creamos una función para convertir valores a binario considerando el siguiente analisis
"""1. Seleccionar un valor decimal
2. Dividirlo entre 2, despues el cociente se divide entre 2 sucesivamente hasta obtener 0. Esto es con division entera (//)
3. Después se obtienen los módulos (%) de las divisiones,que serán valores 0 o 1 
4. Se invierte el orden en la cadena de resultadosy se invierte su orden. Con esto ya tenemos el número binario.
5. En caso de ser un número negativo se hace otra inversion y se añade un 1 adicional en la izquierda inicial"""


def conversor_binario(numero, max_bits=9):
    
    #Si no se reciben numeros, regresamos un valor nulo
    if numero == 0:
        return 0
    
    #Creamos nuestro contenedor vacio para almacenar la cadena de valores binarios
    cadena_binaria = ""

    #Obtenemos el valor absoluto de cada numero
    absoluto = abs(numero)
    
    for _ in range(max_bits - 1):
        cadena_binaria = str(absoluto % 2) + cadena_binaria
        #Cosciente
        absoluto //= 2
    
    #Se tiene que considerar que los valores negativos deben invertir la cadena, y al principio de esta debe ponerse un 1
    if numero < 0:
        #Cremos una cadena que reemplaza de manera invertida 0 y 1
        inversor = ''.join(['1' if bit == '0' else '0' for bit in cadena_binaria])
        carry = 1
        #Cremos un nuevo contenedor para nuestro string binario
        invertido = ""
        for bit in inversor[::-1]:
            current_bit = str((int(bit) + carry) % 2)
            carry = (int(bit) + carry) // 2
            invertido = current_bit + invertido
        cadena_binaria = '1' + invertido
    
    else:
        indicador = False
        while indicador is False:
            valor_inicial = cadena_binaria[0]
            if valor_inicial == "1":
                indicador = True
            else:
                #Añadimos los valores con el slicing
                cadena_binaria = cadena_binaria[1:]

    return cadena_binaria


# In[2]:


#Creamos una función para convertir valores a hexadecimal considerando el siguiente analisis
"""1. Seleccionar un valor decima
2. Dividirlo entre 16, despues el cociente se divide entre 16 sucesivamente hasta obtener 0. Esto es con division entera (//)
3. Después se obtienen los módulos (%) de las divisiones,que serán dentro de nuestro diccionario hexadecimal
4. Se invierte el orden en la cadena de resultados y se invierte su orden. Con esto ya tenemos el número binario."""

def conversor_hexa(numero): 

    if numero == 0:
        return 0

    if numero < 0:
        diccionario = "0123456789ABCDEF"
        #Creamos nuestro contenedor de cadena hexadecimal
        cadena_hexa = ""
        #El operador Bitwise << es análogo al >> con la diferencia que en este caso el desplazamiento es realizado a la izquierda.0001, <<3, 1000.
        #Recorremos los bits al tratarse de un valor negativo
        numero = (1 << 32) + numero  
        while numero > 0:
            #Modulo
            modulo = numero % 16
            cadena_hexa = diccionario[modulo] + cadena_hexa
            #Absoluto
            numero //= 16
        return cadena_hexa
    else:
        diccionario = "0123456789ABCDEF"
        cadena_hexa = ""
        while numero > 0:
            modulo = numero % 16
            cadena_hexa = diccionario[modulo] + cadena_hexa
            numero //= 16
        return cadena_hexa


# In[19]:


def impresora(ruta):
    
    try:
        #Iniciamos nuestro timer
        timer = time.time()
        with open(ruta, 'r', encoding="utf-8") as archivo:
            # Creamos una lista contenedora de numeros
            lista_numeros = []
            for renglon in archivo:
                lista_numeros.append(renglon.strip())

            arreglo_base = []

            for num in lista_numeros:
                diccionario = {}
                try:
                    entero = int(num)
                    diccionario['DECIMAL'] = entero
                    binary = conversor_binario(entero)
                    diccionario['BINARIO'] = binary
                    hexadecimal = conversor_hexa(entero)
                    diccionario['HEXADECIMAL'] = hexadecimal
                    #arreglo_base = [].append(diccionario)
                    arreglo_base.append(diccionario)
                
                except ValueError:
                    error_value = "#VALUE!"
                    diccionario['DECIMAL'] = num
                    diccionario['BINARIO'] = error_value
                    diccionario['HEXADECIMAL'] = error_value
                    #arreglo_base = [].append(diccionario)
                    arreglo_base.append(diccionario)

            #Creamos el arreglo final, incluyendo encabezados
            arreglo_final = "INDICE	DECIMAL	BINARIO	HEXADECIMAL \n"

            for index, diccionario in enumerate(arreglo_base):
                arreglo_final += (
                    f"{index+1} {diccionario['DECIMAL']} "
                    f"{diccionario['BINARIO']} {diccionario['HEXADECIMAL']}\n"
                )

            fin = time.time()
            temporizador_final = (fin - timer) * 1000

            print(arreglo_final)
            print("\n")
            tiempo_total = f"Tiempo de ejecución: {temporizador_final:.6f} milisegudos"
            print(tiempo_total)
            #Creamos el archivo resultante
            with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
                print(arreglo_final, file=file)
                print("\n", file=file)
                print(tiempo_total, file=file)


    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' No se encuentra.")


# In[20]:


#Para fines de observar resultados invocamos el archivo desde una ruta local, posteriormente queda la opción de invocarlo desde consola
impresora("C:/Users/traba/Downloads/TC1.txt")
#impresora("C:\Users\traba\Downloads\TC1.txt")


# In[ ]:


if __name__ == "__main__":
    # Verificamos los parametros en la linea de comando, en caso de estar vacía, solicitamos la información
    if len(sys.argv) != 2:
        print("Introduce la ruta como se muestra: python compute_statistics.py P1/TC2.txt")
        sys.exit(1)

    # obtenemos la ruta de los archivos
    ruta_archivo = sys.argv[1]

    # Invocamos nuestra función principal para imprimir las estadisticas
    impresora(ruta_archivo)


# In[ ]:




