from functools import reduce
import random

def process_matrix(matrix):
    """
    recibe una matriz (lista de listas) con valores numéricos, y devuelve otra matriz de la misma longitud en la que cada elemento 
    ha cambiado por el promedio de su valor y el valor de sus vecinos
    """

    #Creo una matriz vacia que será el resultado:
    processed_matrix = []
    #Creo un bucle que me va a recorrer todos los elementos
    #Primero recorre las listas de la matriz
    for i, column in enumerate(matrix):
        #Creo una lista vacía
        processed_column = []
        #Despues cada elemento de esa lista
        for j, value in enumerate(column):
            #Proceso el elemento:
            processed_element = process_element(i, j, matrix)
            #Añado el elemento a la lista
            processed_column.append(processed_element)
        #Añado la columna a la matriz
        processed_matrix.append(processed_column)
    #Una vez fuera del loop devuelvo la matriz procesada
    return processed_matrix

def process_element(column, row, matrix):
    """ 
    Recibe la posicion de un elemento en una matriz, calcula el promedio con sus vecinos y devuelve dicho promedio
    """
    #Obtengo una lista con las coordenadas de todos los vecinos:
    coordinates = get_coordinates(column, row, matrix)
    #Creo una lista de los valores con esas coordenadas:
    values = get_values(coordinates, matrix)
    #Calculo su promedio:
    Avergs = get_averages(values)
    #Devuelvo el valor final
    return Avergs

def get_coordinates(i, j, matrix):
    """
    Recibe unas coordenadas y una matriz, devuelve una lista con las coordenadas de los vecinos 
    """
    #Creo la lista de coordenadas, con la coordenada que he recibido ya metida
    list_of_coordinates = [[i,j]]
    #Voy añadiendo a los vecinos
    list_of_coordinates.append([i-1,j])
    list_of_coordinates.append([i+1,j])
    list_of_coordinates.append([i,j+1])
    list_of_coordinates.append([i,j-1])

    #elimino los indices imposibles
    #x[0] sera la i(me dice que lista, o columna,  dentro de la matriz), x[1] la j(me dice que elemento dentro de la lista): 
    # i tiene que ser mayor o igual que 0 y menor que el len de la matriz,
    # la j tiene que ser mayor o igual que cero y menor que el len de la lista en la que se encuentra
    list_of_coordinates = filter(lambda x: x[0] >= 0 and x[0] < len(matrix) and x[1] >= 0 and x[1] < len (matrix[x[0]]), list_of_coordinates)

    return list_of_coordinates


def get_values(coordinates, matrix):
    """
    Recibe una lista de coordenadas y una matriz, devuelve una lista con los valores que hay en cada coordenada de la matriz
    """
    #Creo una lista de valores vacia
    list_of_values = []
    #Recorro la lista de coordenadas
    for coordinate in coordinates:
        #Añado a la lista de valores el valor almacenado en la coordenada en matrix
        list_of_values.append(matrix[coordinate[0]][coordinate[1]])

    return list_of_values

def get_averages(values):
    """
    Recibe una lista de valores y devuelve el promedio de esos valores
    """
    
    return reduce(lambda a, b: a+b, values, 0) / len(values)



if __name__ == "__main__":
    
    print("My Matrix\n")
    my_matrix = [[1, 2, 4, 8, 1],
                 [9, 4, 5, 2, 9],
                 [9, 4, 3, 3, 0],
                 [8, 1, 1, 2, 1]]


    for x in my_matrix:
        print(x)
    
    print("\nProcessed matrix\n")


    new_matrix = process_matrix(my_matrix)

    for x in new_matrix:
        print(x)

    print("\nRandom matrix\n")

    random_lenght = random.randint(0, 20)        
    my_matrix_rand = [[random.randint(0,10) for x in range(0,random_lenght) ] for x in range(0, random.randint(0, 20))]

    for x in my_matrix_rand:
        print(x)

    print("\nProcessed random matrix\n")

    new_processed_random = process_matrix(my_matrix_rand)

    for x in new_processed_random:
        print(x)



    print(process_matrix([[1,2,3]]))
    

    
