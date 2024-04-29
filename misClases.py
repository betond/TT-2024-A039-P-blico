#****************************************************
class Individuo:
    def __init__(self):
        self.horario = []
        self.fitness = 0.0
        self.uas = []
        self.docen = []
        self.percla = [[],[],[],[],[]]

#Clases para verificación de restricciones
class Docentes:
    def __init__(self):
        self.id = 0
        self.horasbase = 0
        self.area = 0
        self.grupos = []
        self.sumahoras = 0
        self.breach = 0.0

class UnidadAprendizaje:
    def __init__(self):
        self.id = 0
        self.descripcion = ""
        self.horasTotales = 0
        self.area = 0

class Salon:
    def __init__(self):
        self.id = 0
        self.clasesid = []
        self.breach = 0.0