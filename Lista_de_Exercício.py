1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio **2)
    
circulo = Circulo(3)
area = circulo.calcular_area()
print(f'A área do ciruculo é {area:.2f}')

2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        print(f'O nome do livro é {self.titulo}')
        print(f'O nome do autor é {self.autor}')

livro = Livro('Capitães da Areia', 'Jorge Amado')
livro.detalhes()

3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
        
    
retangulo = Retangulo(2, 2)
area = retangulo.calcular_area()
print(f'A área do retângulo é {area}')

4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo.
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor  
        
    def sacar(self, valor):
        if valor <= self.saldo:  # Verifica se há saldo suficiente
            self.saldo -= valor  # Subtrai o valor do saldo
        else:
            print("Saldo insuficiente.")
    
    def detalhes_da_conta(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.saldo}')
    
contabancaria = ContaBancaria(2000, 'Daniel')
contabancaria.detalhes_da_conta()

contabancaria.depositar(500)
contabancaria.sacar(300)
contabancaria.detalhes_da_conta()

5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")

pessoa1 = Pessoa("Ana", 25)
pessoa1.falar()

6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo de uso:
produto1 = Produto("Camiseta", 50, 3)
total = produto1.calcular_total()
print(f"Total: R$ {total}")

7 Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

# Exemplo de uso:
carro1 = Carro("Toyota", "Corolla", 2021)
print(carro1.detalhes())

8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

# Exemplo de uso:
aluno1 = Aluno("João", [8, 9, 7])
media = aluno1.calcular_media()
print(f"Média: {media}")

9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplo de uso:
triangulo1 = Triangulo(3, 4, 5)
perimetro = triangulo1.calcular_perimetro()
print(f"Perímetro: {perimetro}")

# 10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)


funcionario1 = Funcionario("Maria", 5000, "Gerente")
funcionario1.aumentar_salario(10)
print(f"Novo salário: R$ {funcionario1.salario}")

