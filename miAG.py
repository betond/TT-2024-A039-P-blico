import random
import os
from datetime import datetime
from misClases import Individuo 
from mideap import *
from subprocesos import *
from restricciones import *

#####################################################
#****************************************************
PobGen = []
salones = []
#****************************************************
identificadores = 0
# | Id | Salón | Docente | UA | L | M | X | J | V |
def poblacion(Size, arg_salones, arg_uas, arg_periodos):
    salones = arg_salones
    set_salones(salones)
    setInSize(len(UAs_semestre(arg_uas)))
    initAg(profesor_id, UAs_semestre(arg_uas), arg_periodos)
    global identificadores
    for n in range(Size):
        nuevo = Individuo()
        salon = rand.choice(salones)
        Ind = toolbox.population(1)
        nuevo.horario = [identificadores, salon, Ind]
        for n in range(len(Ind[0])):
            nuevo.uas.append(Ind[0][n][1])
        for n in range(len(Ind[0])):
            nuevo.docen.append(Ind[0][n][0])
        for c in range(len(Ind[0])):
            i=0
            for p in range(len(Ind[0][c][2:])):
                nuevo.percla[p].append(Ind[0][c][2+i])
                i += 1
        #
        #Ind = toolbox.population(1)
        #nuevo.horario = [n, salones[n], Ind]
        #-print(nuevo.uas)
        #
        identificadores += 1
        PobGen.append(nuevo)

def fitness():
    for ind in PobGen:
        master_horario(ind.horario[2][0])
        sum_hor(ind.horario[2][0])
        salon_horario(ind.horario)
    set_breach_docentes()
    for ind in PobGen:
        ind.fitness = aptitud(ind) + Salon_Salon(ind)
#--------------------- Operaciones ----------------------
def ordenar():
    PobGen.sort(key=lambda Individuo: Individuo.fitness)
    #print("\n\t\tOrdenados  ----  " + str(len(PobGen)))
    
def elitismo(num_grupos, arg_salones, arg_uas, arg_periodos):
    global PobGen
    if len(PobGen) <= num_grupos:
        #print("\n\n\t\tNo podemos hacer esto\n\n")
        poblacion(num_grupos*2, arg_salones, arg_uas, arg_periodos)
        #print(len(PobGen))
        limpiar_fit()
        fitness()
    if len(PobGen) > num_grupos:
        prom = 0
        for x in PobGen:
            prom += x.fitness
        #print( "\t\t\t" + str(prom))
        prom = prom/len(PobGen)
        print(prom)
        PobGen = [x for x in PobGen if x.fitness <= (prom)]
    #print("\n\t\tEliminados  -- restan --  " + str(len(PobGen)))
    
def cruzamiento(num_grupos,Prob_Cruce):
    # print(Prob_Cruce)
    # print(num_grupos)
    # print(num_grupos*Prob_Cruce)
    for _ in range(int(random.randint(0,5) * Prob_Cruce)):
        i = random.randint(0,len(PobGen)-1)
        j = random.randint(0,len(PobGen)-1)
        k = (len(PobGen) * int(num_grupos * Prob_Cruce)) % 10
        #print("\n\t\tCruzados  ------------ " + str(i) + "----" + str(j)) 
        # print(PobGen[i].horario)
        # print(PobGen[j].horario)
        if k <= 1:
            n_ind1, n_ind2 = uaXua(PobGen[i],PobGen[j])
        elif k > 1 and k <= 2:
            n_ind1, n_ind2 = docenteXdocente(PobGen[i],PobGen[j])
        elif k > 3 and k <= 4:
            n_ind1, n_ind2 = salonXsalon(PobGen[i],PobGen[j])
        elif k > 5 and k <= 6:
            n_ind1, n_ind2 = diasXdias(PobGen[i],PobGen[j])
        else:
            n_ind1 = PobGen[i]
            n_ind2 = PobGen[j]
        PobGen[i] = n_ind1
        PobGen[j] = n_ind2
        # print(PobGen[i].horario)
        # print(PobGen[j].horario)

def mutacion(num_grupos,Prob_Mut,arg_salones, arg_uas, arg_periodos):
    # print(Prob_Mut)
    # print(num_grupos)
    # print(num_grupos*Prob_Mut)
    for _ in range(int(random.randint(0,5) * Prob_Mut)):
        i = random.randint(0,len(PobGen)-1)
        j = (len(PobGen) * int(num_grupos * Prob_Mut)) % 10
        if j <= 1:
            n_ind = Mua(PobGen[i],arg_uas) #Completo
        elif j > 1 and j <= 2:
            n_ind = Mdias(PobGen[i],arg_periodos) #Completo
        elif j > 3 and j <= 4:
            n_ind = Mdocente(PobGen[i]) #Completo
        elif j > 5 and j <= 6:    
            n_ind = Msalon(PobGen[i],arg_salones) #Completo
        else:
            n_ind = PobGen[i]
        PobGen[i] = n_ind
        #print("\n\t\tMutados  ------------ " + str(i))

#------------ Suboperaciones Cruzamiento ---------------
def uaXua(ind1,ind2):
    r1 = random.randint(1,len(ind1.horario[2][0]))
    r2 = random.randint(1,len(ind2.horario[2][0]))
    # print(str(r1) + "<----->" + str(r2))
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])
    aux = ind1.horario[2][0][r1-1][1]
    # print(aux)
    ind1.horario[2][0][r1-1][1] = ind2.horario[2][0][r2-1][1]
    ind2.horario[2][0][r2-1][1] = aux
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])
    return ind1, ind2

def diasXdias(ind1,ind2):
    r1 = random.randint(1,len(ind1.horario[2][0]))
    r2 = random.randint(1,len(ind2.horario[2][0]))
    # print(str(r1) + "<----->" + str(r2))
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])
    aux = ind1.horario[2][0][r1-1][2:]
    # print(aux)
    ind1.horario[2][0][r1-1][2:] = ind2.horario[2][0][r2-1][2:]
    ind2.horario[2][0][r2-1][2:] = aux
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])    
    return ind1,ind2

def docenteXdocente(ind1,ind2):
    r1 = random.randint(1,len(ind1.horario[2][0]))
    r2 = random.randint(1,len(ind2.horario[2][0]))
    # print(str(r1) + "<----->" + str(r2))
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])
    aux = ind1.horario[2][0][r1-1][0]
    # print(aux)
    ind1.horario[2][0][r1-1][0] = ind2.horario[2][0][r2-1][0]
    ind2.horario[2][0][r2-1][0] = aux
    # print(ind1.horario[2][0][r1-1])
    # print(ind2.horario[2][0][r2-1])
    return ind1, ind2

def salonXsalon(ind1,ind2):
    # print(ind1.horario[1])
    # print(ind2.horario[1])
    aux = ind1.horario[1]
    # print(aux)
    ind1.horario[1] = ind2.horario[1]
    ind2.horario[1] = aux
    # print(ind1.horario)
    # print(ind2.horario)
    return ind1, ind2

#-------------- Suboperaciones Mutación ----------------
def Mua(ind,uas):
    r = random.randint(1,len(ind.horario[2][0])) 
    #print(ind.horario[2][0][r-1])
    ind.horario[2][0][r-1][1] = random.choice(uas)
    #print(ind.horario[2][0][r-1])
    #print(ind.horario)
    return ind

def Mdias(ind,periodos):
    r = random.randint(1,len(ind.horario[2][0])) 
    #print(ind.horario[2][0][r-1])
    rr = random.randint(2,6)
    #print(rr)
    ind.horario[2][0][r-1][rr] = random.choice(periodos)
    #print(ind.horario[2][0][r-1])
    #print(ind.horario)
    return ind

def Mdocente(ind):
    r = random.randint(1,len(ind.horario[2][0])) 
    #print(ind.horario[2][0][r-1])
    ind.horario[2][0][r-1][0] = random.choice(profesor_id)
    #print(ind.horario[2][0][r-1])
    #print(ind.horario)
    return ind

def Msalon(ind,salon):
    #print(ind.horario[1])
    ind.horario[1] = random.choice(salon)
    #print(ind.horario[1])
    #print(ind.horario)
    return ind
#-------------------------------------------------------
def limpiar_fit():

    for ind in PobGen:
        ind.fitness = 0.0
        ind.uas = []
        ind.docen = []
        ind.percla = [[],[],[],[],[]]

    for d in Doc:
        d.grupos = []
        d.sumahoras = 0
        d.breach = 0.0

    for s in Sal:
        s.clasesid = []
        s.breach = 0.0

    for elemento in PobGen:
        Ind = elemento.horario[2]
        for n in range(len(Ind[0])):
            elemento.uas.append(Ind[0][n][1])
        for n in range(len(Ind[0])):
            elemento.docen.append(Ind[0][n][0])
        for c in range(len(Ind[0])):
            i=0
            for p in range(len(Ind[0][c][2:])):
                elemento.percla[p].append(Ind[0][c][2+i])
                i += 1

#*******************************************************
def Salon_Salon(ind): # ---- 1 ---> 5 pts
    breach_ind = 0
    for s in Sal:
        if ind.horario[1] == s.id:
            if len(s.clasesid) > 1:
                s.breach += 5 * len(s.clasesid)
                breach_ind = s.breach
                # print(s.clasesid)
                for n in s.clasesid:
                    for elem in PobGen:
                        if elem.horario[0] == n:
                            elem.fitness += breach_ind
                    #print(PobGen[n].fitness)
            #print(s.id)
            #print(s.clasesid)
            #print(ind.horario[1])
    return breach_ind
#*******************************************************
def imprimir(Turno,semestre,numero,direc):

    fechaH = datetime.now().strftime("%Y-%m-%d-%H-%M")
    
    nombre = semestre+"-"+fechaH

    sol = []
    for e in PobGen:
        y,m,d,h,M,s = int(datetime.now().strftime("%Y")),int(datetime.now().strftime("%m")),int(datetime.now().strftime("%d")),int(datetime.now().strftime("%H")),int(datetime.now().strftime("%M")),int(datetime.now().strftime("%S"))
        if len(str(e.horario[0])+str(y+m+d+h+M+s)+str(numero)) >= 10:
            e.horario[0] = int((str(e.horario[0])+str(y+m+d+h+M+s)+str(numero))[-9:])
        else:
            e.horario[0] = int((str(e.horario[0])+str(y+m+d+h+M+s)+str(numero)))
        #print(e.horario[0])
        sol.append(e.horario)

    data = {i:sol[i] for i in range(0,len(sol))}

    with open(direc+"/"+nombre+".json", "w") as salida:
        json.dump(data,salida)

        #print(e.horario[:2])
    #    print(e.fitness)
        # print(e.uas)
        # print(e.docen)
        # print(e.percla)
    #    for i in range(len(e.horario[2][0])):
    #        prueba = e.horario[2][0][i]
    #        print(prueba)
    # for d in Doc:
    #    print(d.id)
    #    print(d.horasbase)
    #    print(d.area)
    #    print(d.grupos)
        # if d.sumahoras != 0:
        #     print(d.id)
    #        print(d.horasbase)
            # print(d.sumahoras)
            # print(d.grupos)
            # print(d.breach)
    #
    # for s in Sal:
    #     if s.clasesid != []:
    #         print(s.id)
    #         print(s.clasesid)
    ######################################
    # n.0 ----  Telecomunicaciones
    # n.1 ----  Diagnostico y mejoramiento ambiental
    # n.2 ----  Mecatronica
    # n.3 ----  Metodología y control de calidad
