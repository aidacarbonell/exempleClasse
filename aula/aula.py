class Aula:
    def __init__(self, profe, alumnes, aula):
        self._profe = profe
        self._alumnes = alumnes
        self._aula = aula
        print("Aula creada")
        
    @property
    def profe(self):
        return self._profe
    
    @property
    def alumnes(self):
        return self._alumnes
    
    @property
    def aula(self):
        return self._aula
        
    def __str__(self):
        al = "\n"
        for a in self.alumnes:
            al = al + "\t" + str(a) + "\n"
        return f"Aula: {self.aula} \n\t{self.profe}" + al