from funcionario import Funcionario
class Professor(Funcionario):
    def __init__(self, nome, cpf, idade, matricula, curso, semestre):
        super().__init__(nome, cpf, idade)
        self.curso = curso
        self.semestre = semestre
        self.matricula = matricula

    def __str__(self):
        return f"{super() .__str__()}, matricula {self.matricula}: {self.matricula}, curso: {self.curso}, semestre: {self.semestre}"