#Exemplo de composição: carro e Motor
class Motor:
    def __init__(self,potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor de {self.potencia} cavalos está ligado."

class Carro:
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia_motor) #Composição: O carro contém o motor

    def ligar_carro(self):
        return f"{self.marca} {self.modelo}: {self.motor.ligar()}"

#Exemplo de agregação: Curso e estudantes
class Estudante:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nome_curso):
        self.nome_curso = nome_curso
        self.estudantes = [] #agregação: O curso mantém uma lista de estudantes, mas os estudantes existem independentemente

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def listar_estudantes(self):
        if self.estudantes:
            return [estudante.nome for estudante in self.estudantes]
        return "Nenhum estudante matriculado."

#Exemplo de uso
if __name__ == "__main__":
    #Composição: Carro e Motor
    carro1 = Carro(marca="Toyota", modelo="Corolla", potencia_motor=132)
    print(carro1.ligar_carro())
    #agregação: curso e estudantes
    curso = Curso(nome_curso="Engenharia de Software")
    estudante1 = Estudante(nome="Alice")
    estudante2 = Estudante(nome="Bob")
    #Adicionando estudantes ao curso
    curso.adicionar_estudante(estudante1)
    curso.adicionar_estudante(estudante2)
    #Listando os estudantes do curso
    print(f"Estudantes matriculados no curso {curso.nome_curso}: {curso.listar_estudantes()}")