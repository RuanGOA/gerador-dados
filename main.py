import random as r
import os

arquivo = open('data/nomes.txt', 'r')
nomes = (arquivo.readline()).split(",")
tamanho = len(nomes)

def geraNome():
   num1 = r.randint(0, tamanho)
   num2 = num1
   while(num1 == num2):
      num2 = r.randint(0, tamanho)

   resultado = nomes[num1] + " " + nomes[num2]
   
   return resultado

#NAO POSSUI VALIDACAO(SE É UM CPF REAL OU UM CNPJ)
def geraNumero(n):
   
   resultado = ""
   for i in range(0, n):
      resultado += str(r.randint(0, 9))

   return resultado

def geraCPF():
   return geraNumero(11)

def geraCNPJ():
   return geraNumero(14)

def clear():
   os.system('cls' if os.name == 'nt' else 'clear')

generate = {
   "1": geraNome(),
   "2": geraCPF(),
   "3": geraCNPJ()
}

def menu():
   print("1 - gerar nome")
   print("2 - gerar cpf")
   print("3 - gerar cnpj")
   print("s - sair")

   opcao = input()

   if opcao != "s":
      print()
      
      try:
         output = generate[opcao]
         print(output)
      except KeyError:
         print("Ai tu me quebra xD")
      
      print()
      menu()

menu()