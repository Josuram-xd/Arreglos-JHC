## first part
days = ["lunes", "martes", "miercoles", "jueves", "viernes"]

paswords = [
    ["123", "holi12", "zorras"],
    ["456", "kundial", "contraseña"],
    ["perro128", "matacocis", "codigouwu"]
]

## Second part
print(days[1]) 
print(paswords[1][1])

## Third part 
days.insert(2,"Estructura de datos")
paswords.pop(2)

## Fourth point
print(days.index("Estructura de datos"))
print(paswords[1].index("456"))