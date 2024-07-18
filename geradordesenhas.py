# -*- coding: utf-8 -*-
import random
import string
import sqlite3


# Conectar com banco de dados
con = sqlite3.connect("/home/angelo/RandomGuard/sqlite/sqlite3.db")
table = con.cursor()

# Verificar se a tabela já existe
table.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='senhas'")
if table.fetchone() is None:
    table.execute("CREATE TABLE senhas(usuario TEXT, senha TEXT)")
    print("Tabela criada")
else:
    None
# Insirir o comprimento da senha e o nome
nome = input("Qual é o site que vai utilizar a senha, ou de onde?")
comprimentosenha = int(input("Quantos caracteres você quer que tenha sua senha?"))

# Letras maiúsculas
letrasmais = string.ascii_uppercase
# Letras minúsculas
letramenos = string.ascii_lowercase
# Números
numeros = string.digits
# Caracteres especiais
caracteres_especiais = "!@#$%&*"
# Função que junta todos os caracteres
todososcaracteres = letramenos + letrasmais + numeros + caracteres_especiais

# Gerar senha
senha = ''.join(random.choice(todososcaracteres) for i in range(comprimentosenha))

# Saída
print("Onde vc ira utlizar é ", nome)
print("A senha gerada é:", senha)

#Insire no banco de dados
table.execute("INSERT INTO senhas(local, senha) VALUES(? , ?)", (nome, senha))
con.commit()
print("Dados inseridos com sucesso!")