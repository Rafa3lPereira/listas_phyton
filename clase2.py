import numpy as np

#arreglo=np.array([4,8,15,16,23,42])
#for i in range (len(arreglo)):
#    print(i)

#print(arreglo)


#arreglo=np.array([4,8,15,16,23,42])
#contar_hasta=len(arreglo)
#for i in range (contar_hasta):
#    print(arreglo[i])

#print(arreglo)
import random 
arreglo = []
for i in range (10):
    arreglo.append(random.randint(0,100))

print (arreglo)

arreglo_copy = np.copy(arreglo)

print("Elemento mayor: ", np.max(arreglo_copy))

print("Elemento menor: ", np.min(arreglo_copy))

print("Suma de los elemntos: ", np.sum(arreglo_copy))

print("Promedio de los elementos: ", np.mean(arreglo_copy))

print("Todos los elementos: ", arreglo_copy)