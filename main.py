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
    for i in range(0, len(nombres)):
        print(nombres[i])
        
RegistrarDato()
print(personas)