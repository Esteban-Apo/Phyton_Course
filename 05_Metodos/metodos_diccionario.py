aspectos = {
    "Color de piel" : "Moreno",
    "Edad" : 21,
    "Estura" : 1.77,
    "Mascota" : "Mono",
    "Pareja" : "Isa"
}

#Permite visualizar que llaves contiene un dictionary
keys_view = aspectos.keys()
print(keys_view)

#Obtiene un valor de una clave
obtener_valor = aspectos.get("Edad")
print(obtener_valor)

#Elima una llave y su valor
eliminar_llave = aspectos.pop("Mascota")
print(aspectos)
