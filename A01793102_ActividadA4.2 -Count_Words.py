#!/usr/bin/env python
# coding: utf-8

# In[47]:


#MAESTRÍA EN INTELIGENCIA ARTIFICIAL APLICADA
#Pruebas de software y aseguramiento de la calidad
#Dr. Gerardo Padilla Zárate

#Actividad 4.2. Ejercicio de Programación 1
#CARLOS ENRIQUEZ GORGONIO
#A01793102
#20 de febrero de 2024


# In[45]:


'''Ejercicio 3. Count Words
Detalles:
Req1. The program shall be invoked from a command line. The program shall receive a file as parameter. The file will contain a words (presumable between spaces).
Req 2. The program shall identify all distinct words and the frequency of them (how many times the word “X” appears in the file). The results shall be print on a screen and on a file named WordCountResults.txt.
All computation MUST be calculated using the basic algorithms, not functions or libraries.
Req 3. The program shall include the mechanism to handle invalid data in the file. Errors should be displayed in the console and the execution must continue.
Req 4. The name of the program shall be wordCount.py
Req 5. The minimum format to invoke the program shall be as follows:python wordCount.py fileWithData.txt
Req 6. The program shall manage files having from hundreds of items to thousands of items.
Req 7. The program should include at the end of the execution the time elapsed for the execution and calculus of the data. This number shall be included in the results file and on the screen.
Req 8. Be compliant with PEP8.
'''


# In[14]:


get_ipython().system('pip install pylint')
get_ipython().system('pip install pylint[spelling]')


# In[15]:


import sys
import time


# In[16]:


#Para definir la función de conteo de frecuencia de las palbras, separaremos los renglones con cadenas de texto, en palabras
def frecuencia(renglon):
    
    #Creamos un diccionario vacio
    frecuencia_individual = {}
    
    #Dividimos cada renglon en palabras, separadas por comas
    for cadena in renglon:
        palabras = cadena.split()

        for palabra in palabras:
            # Eliminamos los signos de puntuación, y homologamos las palabras en minuscula
            palabra = palabra.strip('.,!?').lower()

            # aumentamos nuestro indicador de frecuencias
            frecuencia_individual[palabra] = frecuencia_individual.get(palabra, 0) + 1

    return frecuencia_individual


# In[20]:


#Definimos nuestra función que mostrara resultados y generará el archivo
def impresora(ruta):

    try:
        #Iniciamos nuestro timer
        inicio = time.time()
        
        #Abrimos el archivo que se analizará
        with open(ruta, 'r', encoding="utf-8") as archivo:        
            renglones = []
            for index, renglon in enumerate(archivo):
                try:
                    renglones.append(renglon.strip())
                except ValueError:
                    print(f"Error: El archivo tiene valores que no se pueden analizar {index+1}")

            integracion = "Row Labels	Count\n"
            contador = frecuencia(renglones)

            for indice, value in contador.items():
                integracion += f"{indice}: {value}\n"

            sumatoria = sum(contador.values())
            integracion += f"Total Global {sumatoria}"

            fin = time.time()
            tiempo_ejecucion = (fin - inicio) * 1000

            #imprimimos nuestros resultados, para visualizarlos
            print(integracion)
            print("\n")
            tiempo_total = f"Tiempo de ejecución es de: { tiempo_ejecucion:.6f} milisegundos"
            print(tiempo_total)
            
            #Creamos nuestro archivo con los elementos visualizados
            with open("WordCountResults.txt", "w", encoding="utf-8") as file:
                print(integracion, file=file)
                print("\n", file=file)
                print(tiempo_total, file=file)

    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo '{file_path}'")


# In[21]:


#Para fines de observar resultados invocamos el archivo desde una ruta local, posteriormente queda la opción de invocarlo desde consola
impresora("C:/Users/traba/Downloads/TC1.txt")
#impresora("C:\Users\traba\Downloads\TC1.txt")


# In[ ]:


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Introduce la ruta como se muestra: python compute_statistics.py P1/TC2.txt")
        sys.exit(1)
    ruta = sys.argv[1]
    impresora(ruta)

