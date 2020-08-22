# Algoritmos geneticos
'''
Knapsack problem

- Maximizar/minimizar

- Individuos:
    Disposicion de mochila de 15kg con cajitas adentro
    Suponemos 5 cajitas:    |1:5|5:3|4:4|1:1|5:5|
    Individuo 1:            |1:5|5:5|4:4|5:3|
    Individuo 2:            |5:5|5:3|4:4|1:1|

    (peso:valor)            |4|2|5|1|3|

    -- se ordena por este valor: price/weight


- Poblacion
- Generaciones
- Evolucion de la poblacion:
-    Seleccion --> Fitness
-    Cruza (Crossover)
-    Mutacion sirve para variacion within-group, como el orden de las cajas no importa en la mochila, no es necesario hacer mutacion.
-    Tampoco tiene sentido en una mutacion "crear" cajas nuevas, ya que el problema trata de ordenar elementos ya existentes, dentro de una mochila.

.
'''

from math import sqrt
from random import shuffle, randint, random
import numpy as np

class cajita():
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def __str__(self):
        return "{}-{}".format(self.p, self.v)

    def importance(self):
        return self.p/self.v


class mochila():
    #En este caso es la mochila de 15kg:

    def __init__(self, cajitas):
        self.disposicion = cajitas

    #def __init__(self):
     #   self.disposicion = []

    def __str__(self):
        return ', '.join(map(str, self.disposicion))

    def valorMochila(self):
        val = 0
        for i in range(len(self.disposicion)):
            val += self.disposicion[i].importance()

        return val

    def peso(self):
        val = 0
        for i in range(len(self.disposicion)):
            val += self.disposicion[i].p

        return val


class Poblacion():

    def __init__(self):
        self.mochilas = []

    def __str__(self):
        s = []
        for i in self.mochilas:
            s.append(str(i) + '\t' + str(i.valorMochila()))

        return '\n'.join(s)



class AG():

    def __init__(self, cajitas, pob_size=5, max_iter=50):
        self.cajitas = cajitas
        self.pob_size = pob_size
        self.max_iter = max_iter
        self.ini_pob = []
        #self.mutation_rate = 0.1
        self.crossover_rate = 0.9

    def crossover(self, ind1, ind2):
        start = randint(0, len(ind1.disposicion) - 1)
        end = randint(start, len(ind1.disposicion))
#        Mochila = mochila()

        Mochila = mochila(ind1.disposicion[start:end].copy())

        #print("Ind1 disp:", ind1.disposicion)
        #Mochila.disposicion.append(ind1.disposicion[start:end].copy())

        #print(Mochila)

        for cajita in ind2.disposicion:
            if not cajita in Mochila.disposicion:
                Mochila.disposicion.append(cajita)
            if Mochila.peso() > 15:
                Mochila.disposicion.remove(cajita)


        return Mochila



    def compute_converge(self, prev, current):
        sum_p = 0
        for ind in prev.mochilas:
            sum_p += ind.valorMochila()

        sum_c = 0
        for ind in current.mochilas:
            sum_c += ind.valorMochila()

        dif = abs(sum_p - sum_c)

        return dif < 0.00001


    def start(self):
        # Crear la poblacion inicial
        self.ini_pob = Poblacion()
        for i in range(self.pob_size):
            stop = 0
            c = self.cajitas.copy()
            #print (self.cajitas[0])
            shuffle(c)
            mochtemp = mochila([])

            while mochtemp.peso() < 15 and stop < 1:

                for z in range(len(c)):
                    mochtemp.disposicion.append(c[z])
                    print("Peso para la mochila:", i, "es", mochtemp.peso())
                    if mochtemp.peso() > 15:
                        mochtemp.disposicion.remove(c[z])# = np.delete(mochtemp.disposicion, -1)
                        print("Peso excedido! Elimino el ultimo elemento.")
                        # mochtemp.disposicion.remove(c[z])
                        stop = 1


                   # mochila.
            self.ini_pob.mochilas.append(mochtemp)


        print('-' * 50)
        print("Poblacion Inicial:")
        print(self.ini_pob)
        print('-' * 50)

        # Comienza la iteracion de generaciones
        current_pob = Poblacion()
        current_pob.mochilas = self.ini_pob.mochilas.copy()

        generation = 0
        converge_count = 0

        while generation < self.max_iter and converge_count < self.max_iter * 0.15:
            generation += 1
            new_pob = Poblacion()

            # Todos los ind. actuales pasan "temporalmente" a la nueva
            # poblacion
            for moc in current_pob.mochilas:
                new_pob.mochilas.append(moc)

            if random() < self.crossover_rate:
                print('**** Crossover ****')
                i1 = current_pob.mochilas[randint(0, len(current_pob.mochilas) - 1)]
                i2 = current_pob.mochilas[randint(0, len(current_pob.mochilas) - 1)]

                new_mochila = self.crossover(i1, i2)
                new_pob.mochilas.append(new_mochila)

            new_pob.mochilas = sorted(new_pob.mochilas, key=lambda i: i.valorMochila(), reverse= True)

            new_pob.mochilas = new_pob.mochilas[:self.pob_size]


            print("Poblacion generacion " + str(generation))
            print(new_pob)
            print('-'*50)


            converge = self.compute_converge(current_pob, new_pob)
            if converge:
                converge_count += 1
            else:
                converge_count = 0

            current_pob = new_pob


ag = AG([cajita(5,5),cajita(5,3),cajita(5,4), cajita(4,6), cajita(6,4)], 5)

ag.start()



#print(cajita(1,5).importance())
#print(cajita(5,3).importance())
#print(cajita(4,4).importance())

#mochila1 = mochila([cajita(5,5), cajita(5,3), cajita(5,4)])
#mochila2 = mochila([cajita(4,5), cajita(6,3), cajita(5,4)])
#mochila3 = mochila([cajita(8,5), cajita(2,3), cajita(5,4)])
#print(mochila1.valorMochila())

#Poblacion1 = Poblacion([mochila1, mochila2, mochila3])

#print(Poblacion1)