from aula.aula import Aula
from aula.persona import Alumne
from aula.persona import Professor

if __name__ == "__main__":
    print("hola")
    
    persona1 = Alumne.pers("AAA", 10, "1r")
    persona2 = Alumne.pers("BBB", 20, "2n")
    persona3 = Professor.pers("CCC", 30, "M03")
    
    print(persona1)
    print(persona2)
    print(persona3)
    
    aula1 = Aula(persona3, {persona1, persona2}, "I01")
    print(aula1)