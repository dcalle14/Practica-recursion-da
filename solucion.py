def buscar_pelicula(lista, titulo, inicio=0, fin=None):
    
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return None  

    medio = (inicio + fin) // 2
    
    if lista[medio]["titulo"] == titulo:
        return lista[medio]
    elif lista[medio]["titulo"] < titulo:
        return buscar_pelicula(lista, titulo, medio + 1, fin)
    else:
        return buscar_pelicula(lista, titulo, inicio, medio - 1)


peliculas = [
    {"titulo": "Avengers", "categoria": "Acción", "precio": 10},
    {"titulo": "Batman", "categoria": "Acción", "precio": 12},
    {"titulo": "Son como niños", "categoria": "Humor", "precio": 8},
]

print(buscar_pelicula(peliculas, "Batman"))


def contar_peliculas_precio(lista, resultado=None, index=0):
    
    if resultado is None:
        resultado = {}

    if index >= len(lista):
        return {contador: {"cantidad": datos["cantidad"], "precio_promedio": datos["total"] / datos["cantidad"]} 
                for contador, datos in resultado.items()} 

    pelicula = lista[index]
    categoria = pelicula["categoria"]
    
    if categoria not in resultado:
        resultado[categoria] = {"cantidad": 0, "total": 0}
    
    resultado[categoria]["cantidad"] += 1
    resultado[categoria]["total"] += pelicula["precio"]

    return contar_peliculas_precio(lista, resultado, index + 1)



print(contar_peliculas_precio(peliculas))


def quicksort_peliculas(lista):
    
    if len(lista) <= 1:
        return lista  
    
    pivote = lista[0]
    menores = [x for x in lista[1:] if x["precio"] <= pivote["precio"]]
    mayores = [x for x in lista[1:] if x["precio"] > pivote["precio"]]

    return quicksort_peliculas(menores) + [pivote] + quicksort_peliculas(mayores)


print(quicksort_peliculas(peliculas))


def buscar_por_precio(lista, min_precio, max_precio, index=0, resultado=None):
    
    if resultado is None:
        resultado = []

    if index >= len(lista):
        return resultado  

    if min_precio <= lista[index]["precio"] <= max_precio:
        resultado.append(lista[index])

    return buscar_por_precio(lista, min_precio, max_precio, index + 1, resultado)


print(buscar_por_precio(peliculas, 8, 12))


def recomendar_peliculas(lista, categoria, index=0, resultado=None):
    if resultado is None:
        resultado = []

    if index >= len(lista):
        return resultado  

    if lista[index]["categoria"] == categoria:
        resultado.append(lista[index])

    return recomendar_peliculas(lista, categoria, index + 1, resultado)


print(recomendar_peliculas(peliculas, "Acción"))
