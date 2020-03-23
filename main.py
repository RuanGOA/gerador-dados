import random as r

arquivo = open('data/nomes.txt', 'r')
nomes = (arquivo.readline()).split(",")
tamanho = len(nomes)

def menu():
   print("1 - gerar nome")
   print("2 - gerar cpf")
   print("3 - gerar cnpj")
   print("s - sair")

   opcao = input()
   resp = 1

   if(opcao == "1"):
      print(geraNome())

   elif(opcao == "2"):
      print(geraNumero(11))

   elif(opcao == "3"):
      print(geraNumero(14))

   elif(opcao == "s"):
      print("saindo")
      resp = 0
   
   else:
      print("Ai tu me quebra xD")
   
   print("------------------------------")

   return resp

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

resposta = 1
while(resposta == 1):
   resposta = menu()