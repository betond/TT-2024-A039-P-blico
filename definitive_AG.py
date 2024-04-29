import random
import sys
from miAG import poblacion,fitness,PobGen, elitismo,mutacion, ordenar, imprimir, cruzamiento, limpiar_fit,ceros

def definitive_AG(num_grupos, arg_salones, arg_periodos, arg_uas, Prob_Cruce, Prob_Mut, Num_Generaciones,Turno,semestre,numero,directorio):
    #ceros()
    if num_grupos == 0:
        return
    
    i = 0
    TamPobla =  num_grupos * 10
    poblacion(TamPobla, arg_salones, arg_uas, arg_periodos)
    while True:
        fitness()
        
        ordenar()

        elitismo(num_grupos, arg_salones, arg_uas, arg_periodos)

# Considera dos individuos seleccionados (Ind_X <-> Ind_Y)
# La cruza contempla {Unidad de Aprendizaje, Docente y Salón}
        cruzamiento(num_grupos,Prob_Cruce)
# Considera un individuo seleccionado (Ind_X)
# La mutación contempla {Unidad de Aprendizaje, Periodos de clase [L,M,X,J,V] ,Docente y Salón}
        mutacion(num_grupos,Prob_Mut, arg_salones, arg_uas, arg_periodos)
        
        if len(PobGen) == num_grupos:
            imprimir(Turno,semestre,numero,directorio)
            print("Grupos objetivo")
            break
        if Num_Generaciones == i:
            imprimir(Turno,semestre,numero,directorio)
            print("Número máximo de generaciones alcanzado")
            break
        
        limpiar_fit()
        i += 1
        print(i)