arquivo = open('data/nomes-censos-ibge.csv', 'r')
novoArquivo = open('data/nomes.txt', 'a')

linhas = arquivo.readlines()

for i in range(1, len(linhas)):

   linha = linhas[i].split(",")
   novoArquivo.write(linha[0] + ",")

novoArquivo.close()