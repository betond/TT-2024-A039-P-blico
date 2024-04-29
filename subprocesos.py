import random
from misClases import Docentes, UnidadAprendizaje, Salon
import json
#####################################################
uacomp = []
#-----------------------------------------------------------------------------------------------------------------------------------------
#with open("/home/El-Gran-N/TT-2022-A039-code/miAG/datos/unidades_aprendizaje.json", "r") as uas:
with open("/home/TB-N/TT-2022-A039-code/miAG/datos/unidades_aprendizaje.json", "r") as uas:
    UAs = json.load(uas)

#with open("/home/El-Gran-N/TT-2022-A039-code/miAG/datos/docentes.json", "r") as doc:
with open("/home/TB-N/TT-2022-A039-code/miAG/datos/docentes.json", "r") as doc:
    docen = json.load(doc)
#-----------------------------------------------------------------------------------------------------------------------------------------
def set_salones(arg_salones):
    global salones
    salones = arg_salones
#*******************************************************
def set_breach_docentes():
    Salon_Docente()
    for d in Doc:
        if d.horasbase >= d.sumahoras:
            d.breach += (d.horasbase - d.sumahoras) * (0.01)
        elif d.horasbase < d.sumahoras:
            d.breach += (d.horasbase - d.sumahoras) * (-0.01)

#-----------------------------------------------------------------------------------------------------------------------------------------
Materias = []
ua_id = []
for unidad, detalles in UAs["unidades_aprendizaje"].items():
    nuevo = UnidadAprendizaje()
    nuevo.id = detalles["ua_id"]
    ua_id.append(detalles["ua_id"])
    nuevo.area = detalles["area_id"]
    nuevo.descripcion = detalles["ua_des"]
    nuevo.horasTotales = detalles["ua_horat"]
    Materias.append(nuevo)
    ua_descripcion = detalles["ua_id"]
    uacomp.append(ua_descripcion)

Doc = []
profesor_id = []    
for d, detalles in docen["docentes"].items():
    nuevo = Docentes()
    nuevo.id = detalles["profesor_id"]
    profesor_id.append(detalles["profesor_id"])
    nuevo.horasbase = detalles["profesor_hrs_bas"]
    nuevo.area = detalles["area"]
    Doc.append(nuevo)

Sal = []
salones = []
for s in salones:
    nuevo = Salon()
    nuevo.id = s
    salones.append(s)
    Sal.append(nuevo)

#-----------------------------------------------------------------------------------------------------------------------------------------
def UAs_semestre(arg_uas):
    coinci = []
    for elemento in uacomp:
        if elemento in arg_uas:
            coinci.append(elemento)
    return coinci

def master_horario(ind):
    for c in ind:
        for d in Doc:
            if c[0] == d.id:
                d.grupos.append(c)

def sum_hor(ind):
    for c in ind:
        for d in Doc:
            if c[0] == d.id:
                d.sumahoras = 0
                for g in d.grupos:
                    d.sumahoras += (5 - g[3:].count(""))

def salon_horario(ind):
    for s in Sal:
        if ind[1] == s.id:
            s.clasesid.append(ind[0])

###########################################################################
def Salon_Docente(): # ---- 2  ---> 20 pts
    for d in Doc:
        breach_ind = 0
        if len(d.grupos) > 1:
            i = 0
            j = 0
            for i in range(len(d.grupos)):
                if i == len(d.grupos)-1:
                    break
                for j in range(len(d.grupos)-1):
                    j += i + 1
                    if j == len(d.grupos):
                        break
                    for k in range(5):
                        if d.grupos[i][k+2] == "":
                            breach_ind += 0.0
                        elif d.grupos[i][k+2] == d.grupos[j][k+2]:
                            breach_ind += 20.0
                    j += 1
                i += 1
            d.breach = breach_ind