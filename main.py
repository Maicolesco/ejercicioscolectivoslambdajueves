personas = []
datos = {
    "nombre",
    "id",
    "tel"
}
def RegistrarDato():
    for i in range(0, 2):
        nombre = input("Digite el nombre: ")
        id = int(input("Digite el id: "))
        tel = int(input("Digite el telefono: "))
        datos = {"nombre": nombre, "id": id, "tel": tel}
        personas.append(datos)

def MostrarNombres(nombres):
        nombres = input("Digite nombre 1: ")
        nombres = input("Digite nombre 2: ")
        nombres = input("Digite nombre 3: ")
        nombres = input("Digite nombre 4: ")
        nombres = input("Digite nombre 5: ")
        nombres = input("Digite nombre 6: ")
        nombres = input("Digite nombre 7: ")
        nombres = input("Digite nombre 8: ")
        
RegistrarDato()
print(personas)