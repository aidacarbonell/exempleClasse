class Persona:
    def __init__(self, nom, edat):
        self._nom = nom
        self._edat = edat
        
    @property
    def nom(self):
        return self._nom
    
    @property
    def edat(self):
        return self._edat
    
    def __str__(self):
        return type(self).__name__ + f": {self.nom}, edat: {self.edat}"
    
class Alumne(Persona):
    def __init__(self, nom, edat, curs):
        super().__init__(nom, edat)
        self._curs = curs
        
    @property
    def curs(self):
        return self._curs
        
    def __str__(self):
        return  super().__str__() + f", curs: {self.curs}"
    
    @classmethod
    def pers(classe, nom, edat, curs):
        return classe(nom, edat, curs)
    
class Professor(Persona):
    def __init__(self, nom, edat, modul):
        super().__init__(nom, edat)
        self._modul = modul
        
    @property
    def modul(self):
        return self._modul
        
    def __str__(self):
        return  super().__str__() + f", curs: {self.modul}"
    
    @classmethod
    def pers(classe, nom, edat, modul):
        return classe(nom, edat, modul)