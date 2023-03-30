def sumar (numeros):
    suma=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]
    return (suma)
    
numeros = []
for i in range(5):
  num = int(input("Ingresa el número {}: ".format(i+1)))
  numeros.append(num)

resultado=sumar(numeros)
print("Los números ingresados son: ", resultado)