from pessoa import Pessoa
from funcionario import Funcionario
from aluno import Aluno
p1 = Pessoa("HENRIQUE", "06988933107", 18)

print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
print(p1)

f1 = Funcionario("jose", "456", 40, "0099", 2526.45, "biblioteca")
print(f1.get_nome())
print(f1)


a1 = Aluno("joao", "456", 20, "0099", "cdc", "21800183")
print(a1)