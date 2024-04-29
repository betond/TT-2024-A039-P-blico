import random as rand
from deap import base
from deap import creator
from deap import tools
from subprocesos import *
    
size = 0

# | Id | Salón | Docente | UA | Periodo | L | M | X | J | V |
#Configuración del Algoritmo
Num_Periodos = ""

def setInSize(n):
    global size
    size = n

#Definición del tipo de problema
creator.create("FitnessMin", base.Fitness , weights=(-1.0,))

#Definición del individuo del AG
creator.create("Individual", list, fitness=creator.FitnessMin)

#Funciones de la Toolbox del AG
toolbox = base.Toolbox()

def initAg(arg_prof, arg_uas, arg_periodos):
    #Conjuntos de Datos
    toolbox.register("attr_Docentes", rand.choice,arg_prof)
    toolbox.register("attr_UA", rand.choice, arg_uas)
    toolbox.register("attr_L",  rand.choice, arg_periodos)
    toolbox.register("attr_M",  rand.choice, arg_periodos)
    toolbox.register("attr_X",  rand.choice, arg_periodos)
    toolbox.register("attr_J",  rand.choice, arg_periodos)
    toolbox.register("attr_V",  rand.choice, arg_periodos)

    #toolbox.register("tipo", función de generación, rango de generación, dimensión del individuo)
    toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_Docentes, toolbox.attr_UA,toolbox.attr_L, toolbox.attr_M, toolbox.attr_X, toolbox.attr_J, toolbox.attr_V), 1)

    toolbox.register("group", tools.initRepeat, list, toolbox.individual, size)

    toolbox.register("population", tools.initRepeat, list, toolbox.group)