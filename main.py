from definitive_AG import *
import json
import os
from datetime import datetime

semestres = {}

#with open("/home/El-Gran-N/TT-2022-A039-code/miAG/datos/plantillas.json","r") as plantillas:
with open("/home/TB-N/TT-2022-A039-code/miAG/datos/plantillas.json","r") as plantillas:
    plan = json.load(plantillas)
    semestres.update({1:plan["1"],2:plan["2"],3.0:plan["3.0"],3.1:plan["3.1"],3.2:plan["3.2"],3.3:plan["3.3"],4.0:plan["4.0"],4.1:plan["4.1"],4.2:plan["4.2"],4.3:plan["4.3"],5.0:plan["5.0"],5.1:plan["5.1"],5.2:plan["5.2"],5.3:plan["5.3"],6.0:plan["6.0"],6.1:plan["6.1"],6.2:plan["6.2"],6.3:plan["6.3"]})
        
    # for par in semestres:
    #     print(par)
    #     print(semestres[par])

#with open("/home/El-Gran-N/TT-2022-A039-code/miAG/datos/conf.json", "r") as AG_data:
with open("/home/TB-N/TT-2022-A039-code/miAG/datos/conf.json", "r") as AG_data:
    gh = json.load(AG_data)

#with open("/home/El-Gran-N/TT-2022-A039-code/miAG/datos/class.json","r") as classs:
with open("/home/TB-N/TT-2022-A039-code/miAG/datos/class.json","r") as classs:
    class_info = json.load(classs)
#Total de salones 56

fechaH = datetime.now().strftime("%Y-%m-%d-%H-%M")
ruta = os.getcwd()

p1 = gh["Primero"] + sum(gh["Tercero"]) + sum(gh["Quinto"])
p2 = gh["Segundo"] + sum(gh["Cuarto"]) + sum(gh["Sexto"])
directorio = ruta+"/Salidas/"+fechaH+"-"+gh["Turno"]

if (p1 != 0 and (gh["Periodo"] == 1)) or (p2 != 0 and  (gh["Periodo"] == 2)):
    if not os.path.exists(directorio):
        os.mkdir(directorio)



def primero(Turno,salones):
    # 1
    print("\n\n\t\t\tEjecución primer semestre\n\n")
    definitive_AG(gh["Primero"], salones, Turno, semestres[1], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"1",1,directorio)

def segundo(Turno,salones):
    # 2
    print("\n\n\t\t\tEjecución segundo semestre\n\n")
    definitive_AG(gh["Segundo"], salones, Turno, semestres[2], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"2",2,directorio)

def tercero(Turno,salones):
    # 3.0 3.1 3.2 3.3
    print("\n\n\t\t\tEjecución tercer semestre\n")
    print("\t\tTelecomunicaciones \n\n")
    definitive_AG(gh["Tercero"][0], salones[0:gh["Tercero"][0]], Turno, semestres[3.0], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"3-Tele",3,directorio)
    print("\n\n\t\tDiagnostico y mejoramiento ambiental \n\n")
    definitive_AG(gh["Tercero"][1], salones[gh["Tercero"][0]:gh["Tercero"][0]+gh["Tercero"][1]], Turno, semestres[3.1], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"3-Ambiental",3,directorio)
    print("\n\n\t\tMecatronica \n\n")
    definitive_AG(gh["Tercero"][2], salones[gh["Tercero"][0]+gh["Tercero"][1]:gh["Tercero"][0]+gh["Tercero"][1]+gh["Tercero"][2]], Turno, semestres[3.2], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"3-Meca",3,directorio)
    print("\n\n\t\tMetodología y control de calidad \n\n")
    definitive_AG(gh["Tercero"][3], salones[gh["Tercero"][0]+gh["Tercero"][1]+gh["Tercero"][2]:gh["Tercero"][0]+gh["Tercero"][1]+gh["Tercero"][2]+gh["Tercero"][3]], Turno, semestres[3.3], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"3-Control",3,directorio)

def cuarto(Turno,salones):
    # 4.0 4.1 4.2 4.3
    print("\n\n\t\t\tEjecución cuarto semestre\n")
    print("\t\tTelecomunicaciones \n\n")
    definitive_AG(gh["Cuarto"][0], salones[0:gh["Cuarto"][0]], Turno, semestres[4.0], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"4-Tele",4,directorio)
    print("\n\n\t\tDiagnostico y mejoramiento ambiental \n\n")
    definitive_AG(gh["Cuarto"][1], salones[gh["Cuarto"][0]:gh["Cuarto"][0]+gh["Cuarto"][1]], Turno, semestres[4.1], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"4-Ambiental",4,directorio)
    print("\n\n\t\tMecatronica \n\n")
    definitive_AG(gh["Cuarto"][2], salones[gh["Cuarto"][0]+gh["Cuarto"][1]:gh["Cuarto"][0]+gh["Cuarto"][1]+gh["Cuarto"][2]], Turno, semestres[4.2], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"4-Meca",4,directorio)
    print("\n\n\t\tMetodología y control de calidad \n\n")
    definitive_AG(gh["Cuarto"][3], salones[gh["Cuarto"][0]+gh["Cuarto"][1]+gh["Cuarto"][2]:gh["Cuarto"][0]+gh["Cuarto"][1]+gh["Cuarto"][2]+gh["Cuarto"][3]], Turno, semestres[4.3], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"4-Control",4,directorio)

def quinto(Turno,salones):
    # 5.0 5.1 5.2 5.3
    print("\n\n\t\t\tEjecución quinto semestre\n")
    print("\t\tTelecomunicaciones \n\n")
    definitive_AG(gh["Quinto"][0], salones[0:gh["Quinto"][0]], Turno, semestres[5.0], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"5-Tele",5,directorio)
    print("\n\n\t\tDiagnostico y mejoramiento ambiental \n\n")
    definitive_AG(gh["Quinto"][1], salones[gh["Quinto"][0]:gh["Quinto"][0]+gh["Quinto"][1]], Turno, semestres[5.1], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"5-Ambiental",5,directorio)
    print("\n\n\t\tMecatronica \n\n")
    definitive_AG(gh["Quinto"][2], salones[gh["Quinto"][0]+gh["Quinto"][1]:gh["Quinto"][0]+gh["Quinto"][1]+gh["Quinto"][2]], Turno, semestres[5.2], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"5-Meca",5,directorio)
    print("\n\n\t\tMetodología y control de calidad \n\n")
    definitive_AG(gh["Quinto"][3], salones[gh["Quinto"][0]+gh["Quinto"][1]+gh["Quinto"][2]:gh["Quinto"][0]+gh["Quinto"][1]+gh["Quinto"][2]+gh["Quinto"][3]], Turno, semestres[5.3], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"5-Control",5,directorio)

def sexto(Turno,salones):
    # 6.0 6.1 6.2 6.3
    print("\n\n\t\t\tEjecución sexto semestre\n")
    print("\t\tTelecomunicaciones \n\n")
    definitive_AG(gh["Sexto"][0], salones[0:gh["Sexto"][0]], Turno, semestres[6.0], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"6-Tele",6,directorio)
    print("\n\n\t\tDiagnostico y mejoramiento ambiental \n\n")
    definitive_AG(gh["Sexto"][1], salones[gh["Sexto"][0]:gh["Sexto"][0]+gh["Sexto"][1]], Turno, semestres[6.1], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"6-Ambiental",6,directorio)
    print("\n\n\t\tMecatronica \n\n")
    definitive_AG(gh["Sexto"][2], salones[gh["Sexto"][0]+gh["Sexto"][1]:gh["Sexto"][0]+gh["Sexto"][1]+gh["Sexto"][2]], Turno, semestres[6.2], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"6-Meca",6,directorio)
    print("\n\n\t\tMetodología y control de calidad \n\n")
    definitive_AG(gh["Sexto"][3], salones[gh["Sexto"][0]+gh["Sexto"][1]+gh["Sexto"][2]:gh["Sexto"][0]+gh["Sexto"][1]+gh["Sexto"][2]+gh["Sexto"][3]], Turno, semestres[6.3], gh["ProbCruce"],gh["ProbMut"], gh["NumGeneraciones"],gh["Turno"],"6-Control",6,directorio)


def main():
    if gh["Periodo"] == 1:
        Turno = class_info[gh["Turno"]]
        #print(Turno)
        primero(Turno,class_info["Salones"][0:gh["Primero"]])
        tTotal = sum(gh["Tercero"])
        tercero(Turno,class_info["Salones"][gh["Primero"]:gh["Primero"]+tTotal])
        qTotal = sum(gh["Quinto"])
        quinto(Turno,class_info["Salones"][gh["Primero"]+tTotal:gh["Primero"]+tTotal+qTotal])
    elif gh["Periodo"] == 2:
        Turno = class_info[gh["Turno"]]
        #print(Turno)
        segundo(Turno,class_info["Salones"][0:gh["Segundo"]])
        cTotal = sum(gh["Cuarto"])
        cuarto(Turno,class_info["Salones"][gh["Segundo"]:gh["Segundo"]+cTotal])
        sTotal = sum(gh["Sexto"])
        sexto(Turno,class_info["Salones"][gh["Segundo"]+cTotal:gh["Segundo"]+cTotal+sTotal])

if __name__ == "__main__":
    main()