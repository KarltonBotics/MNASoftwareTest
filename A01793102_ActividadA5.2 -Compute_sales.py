#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MAESTRÍA EN INTELIGENCIA ARTIFICIAL APLICADA
#Pruebas de software y aseguramiento de la calidad
#Dr. Gerardo Padilla Zárate

#Actividad 5.2. Ejercicio de programación 2 y análisis estático
#CARLOS ENRIQUEZ GORGONIO
#A01793102
#21 de febrero de 2024


# In[ ]:


'''1. Compute sales
Req1. The program shall be invoked from a command line. The program shall receive two files as parameters. The first file will contain information in a JSON format about a catalogue 
of prices of products. The second file will contain a record for all sales in a company. 
Req 2. The program shall compute the total cost for all sales included in the second JSON archive. The results shall be print on a screen and on a file named SalesResults.txt. The total cost should include all items in the sale considering the cost for every item in the first file. 
The output must be human readable, so make it easy to read for the user.
Req 3. The program shall include the mechanism to handle invalid data in the file. Errors should be displayed in the console and the execution must continue.
Req 4. The name of the program shall be computeSales.py
Req 5. The minimum format to invoke the program shall be as follows: python computeSales.py priceCatalogue.json salesRecord.json
Req 6. The program shall manage files having from hundreds of items to thousands of items.
Req 7. The program should include at the end of the execution the time elapsed for the execution and calculus of the data. This number shall be included in the results file and on the screen.
Req 8. Be compliant with PEP8'''


# In[1]:


get_ipython().system('pip install pylint')
get_ipython().system('pip install pylint[spelling]')
get_ipython().system('pip install flake8')


# In[2]:


import sys
import time
import json


# In[3]:


#Definimos una función que generara la suma de ventas, considerando aquellos que se vendieron mas de 1 vez.
def sumatoria(ventas, catalogo):
    
    #Creamos una variable que integrará la sumatoria
    total = 0
    
    #Recorremos los elementos de nuestra cadena de ventas y nuestro catalogo
    for venta in ventas:
        if venta['Product'] not in catalogo:
            print(f"No se enceuntra el articulo '{venta['Product']}' en el catalogo"
            )
        else:
            articulo = catalogo.get(venta['Product'])
            #Multiplicamos el precio por la cantidad de productos adquiridos
            cuantifica = articulo['price'] * venta['Quantity']
            total = total + cuantifica

    return total


# In[4]:


def impresora(ruta_productos, ruta_ventas):

    #Iniciamos nuestro temporizador
    inicio = time.time()
    
    #Creamos nuestras listas que serviran como argumentos para llamar la función de calculo de ventas
    productos = None
    ventas = None
    
    try:
        #Abrimos el archivo con la lista de productos
        with open(ruta_productos, 'r', encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta '{ruta_productos}'")

    try:
        #Abrimos el archivo con los detalles de las ventas
        with open(ruta_ventas, 'r', encoding="utf-8") as archivo:
            ventas = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta '{ruta_ventas}'")

    catalogo = dict(
        (product['title'], product) for product in productos
    )
    total = sumatoria(ventas, catalogo)

    total_acumulado = (
        f"TOTAL ACUMULADO DE VENTAS: \n"
        f"{total}"
    )

    fin = time.time()
    temporizador = (fin - inicio) * 1000

    print(total_acumulado)
    print("\n")
    tiempo_total = (f"tiempo de ejecución en milisegundos: {temporizador:.6f}")
    print(tiempo_total)
    
    #Imprimimos resultados en un archivo
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        print(total_acumulado, file=file)
        print("\n", file=file)
        print(tiempo_total, file=file)


# In[5]:


#Para fines de observar resultados invocamos el archivo desde una ruta local, posteriormente queda la opción de invocarlo desde consola
impresora("C:/Users/traba/Downloads/TC1P.json","C:/Users/traba/Downloads/TC1S.json")
#impresora("C:\Users\traba\Downloads\TC1.txt")


# In[ ]:


if __name__ == "__main__":
    # si no hay 3 argumentos en nuestra linea de comando inicial, indica la forma de introducirlos
    if len(sys.argv) != 3:
        print("Introduce los parametros y la rutas como se muestra:"
            "python computeSales.py "
            "priceCatalogue.json salesRecord.json"
        )
        sys.exit(1)

    #Creamos las variables que alojan las rutas de los archivos obtenidos como argumentos inciales
    archivo_con_productos = sys.argv[1]
    archivo_con_ventas = sys.argv[2]

    # invocamos nuestra funcion principal
    impresora(archivo_con_productos, archivo_con_ventas)

