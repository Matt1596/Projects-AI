import numpy as np
from neupy import algorithms

def dibujar_imagen(imagen):
    for fila in imagen.tolist():
        print('| ' + ' '.join(' *'[val] for val in fila))


cero = np.matrix([0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0])

uno = np.matrix([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 ])

dos = np.matrix([1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, ])

dibujar_imagen(dos.reshape((6, 5)))


data = np.concatenate([cero, uno, dos], axis=0)

redHopfield = algorithms.DiscreteHopfieldNetwork(mode='sync')

redHopfield.train(data)


#### Definimos patrones rotos:

Cero_roto = np.matrix([0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,])

print("Cero roto:")
dibujar_imagen(Cero_roto.reshape((6, 5)))

print("Tratamos de recuperarlo:")
result = redHopfield.predict(Cero_roto)
dibujar_imagen(result.reshape((6, 5)))

print("Dos roto:")
Dos_roto = np.matrix([1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ])
dibujar_imagen(Dos_roto.reshape((6, 5)))

print("Intentamos recuperarlo:")
result = redHopfield.predict(Dos_roto)
dibujar_imagen(result.reshape((6, 5)))

print("Podemos observar que no se decidio entre el 1 y el 2.")

print("Cambiamos el modo a async y probamos de nuevo:")
redHopfield.mode = 'async'
redHopfield.n_times = 400

result = redHopfield.predict(Dos_roto)
dibujar_imagen(result.reshape((6, 5)))

print("(A veces puede decidirse por 1 en vez de 2, ejecutar de nuevo).")