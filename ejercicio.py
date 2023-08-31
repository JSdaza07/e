class Indice:
    def __init__(self):
        self.__pdelta = 0
        self.__ptheta = 0
        self.__palfa1 = 0
        self.__palfa2 = 0
        self.__pbeta = 0
        self.__pgamma = 0
    def verPdelta(self):
        return self.__pdelta
    def verPtheta(self):
        return self.__ptheta
    def verPalfa1(self):
        return self.__palfa1
    def verPalfa2(self):
        return self.__palfa2
    def verPbeta(self):
        return self.__pbeta
    def verPgamma(self):
        return self.__pgamma
    def asignarPdelta(self,a):
        self.__pdelta = a
    def asignarPtheta(self,b):
        self.__ptheta = b
    def asignarPalfa1(self,c):
        self.__palfa1 = c
    def asignarPalfa2(self,d):
        self.__palfa2 = d
    def asignarPbeta(self,e):
        self.__pbeta = e
    def asignarPgamma(self,f):
        self.__pgamma = f
class Visita:
    def __init__(self):
        self.__fechavisita = ""
        self.__registroe = ""
        self.__notas = ""
        self.__indices = Indice()
    def verFechavisita(self):
        return self.__fechavisita
    def verRegistroe(self):
        return self.__registroe
    def verNotas(self):
        return self.__notas
    def verIndices(self):
        return self.__indices
    def asignarFechavisita(self,g):
        self.__fechavisita = g
    def asignarRegistroe(self,h):
        self.__registroe = h
    def asignarNotas(self,i):
        self.__notas = i
    def asignarIndices(self,j):
        self.__indices = j
class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__visitas = {}
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verVisitas(self):
        return self.__visitas
    def asignarNombre(self,k):
        self.__nombre = k
    def asignarCedula(self,l):
        self.__cedula = l
    def asignarGenero(self,m):
        self.__genero = m
    def asignarVisitas(self,n):
        self.__visitas = n
class Sistema:
    def __init__(self):
        self.__listPac = {}
    def verificarExiste(self,cedula):
        for p in self.__listPac:
            if cedula == p.verCedula():
                return True
            else:
                False
    def ingresarPaciente


    