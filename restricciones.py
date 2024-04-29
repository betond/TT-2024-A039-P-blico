from subprocesos import *

def aptitud(ind):
    return horas_min_semana_ua(ind.horario[2][0]) + horas_min_semana_docente(ind.horario[2][0]) + salon_ua_docente(ind) + peridos_x_dia(ind)

#----------  Restricciones del problema  --------------------
def horas_min_semana_ua(horario): # ---- 3 ---> 15 pts
    breach = 0  # -- penalización de "2"
    for h in horario:
        for m in Materias:
            if m.id == h[1]:
                #print(h)
                horas_actuales = 5 - h[2:].count("")
                if horas_actuales != m.horasTotales:
                    breach += 15
                #print("ACT -- " + str(horas_actuales))
                #print("TOT -- " + str(m.horasTotales))
    #print(breach)
    return breach
    
def horas_min_semana_docente(horario): # ---- 4 ---> n pts
    breach = 0.0  # -- penalización de ".2"
    for h in horario:
        for d in Doc:
            if d.id == h[0]:
                if d.breach < 0.0:
                    breach -= d.breach
                elif d.breach >= 0.0:                     
                    breach += d.breach
            #print(d.breach)
    #print(breach)
    return breach

def salon_ua_docente(ind):  # ---- 5 - 6
    breach = 0  # -- penalización de "10"
    breach = S_U(ind) + U_D(ind)
    return breach

#############################################################

def S_U(ind): # ---- 5 ---> 20 pts
    breach_ind = 0
    for i in ind.uas:
        if ind.uas.count(i) > 1:
            breach_ind += 20
    return breach_ind

def U_D(ind): # ---- 6 ---> 15 pts
    breach_ind = 0
    for n in ind.horario[2][0]:
        for d in Doc:
            if d.id == n[0]:
                for m in Materias:
                    if n[1] == m.id:
                        if m.area != d.area:
                            breach_ind += 15
    return breach_ind

#############################################################

def peridos_x_dia(ind): # ---- 7 ---> 10 pts
    breach_ind = 0
    for d in ind.percla:
        for h in d:
            if d.count(h) > 1:
                if h != "":
                    breach_ind += 10
    return breach_ind