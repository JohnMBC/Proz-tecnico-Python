with open ("dados_de_teste.txt", "r") as arquivo: # Abrindo o arquivo porque quero ler no arquivo
      texto = arquivo.read() # ler o arquivo e armazenar dentro da variavel texto
      print(texto)
 
with open ("dados_de_teste.txt", "w") as arquivo: # Abrindo o arquivo porque quero escrever no arquivo
      arquivo.write ("inserindo texto dentro do arquivo(0)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha
      arquivo.write("Inserindo texto dentro do arquivo(1)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha
      arquivo.write("Inserindo texto dentro do arquivo(2)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha 
      arquivo.write("Inserindo texto dentro do arquivo(4)")# Aqui não usei quebra linha
      arquivo.write ("inserindo texto dentro do arquivo(5)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha
      arquivo.write("Inserindo texto dentro do arquivo(6)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha
      arquivo.write("Inserindo texto dentro do arquivo(7)") # Escrevendo no arquivo
      arquivo.write("\n") # Quebra de linha (comentado para quebra linha)
      arquivo.write("Inserindo texto dentro do arquivo(8)")
with open ("dados_de_venda.txt", "r") as arquivo: # Abrindo o arquivo porque quero ler no arquivo
      texto = arquivo.read() # ler o arquivo e armazenar dentro da variavel texto
      print(texto.split("\n"))# method pega texto e separa cada item de acordo com (?) "enter"
      #vira uma lista onde cada item da lista é um a linha(vira um array)
      lista_texto = texto.split("\n")# Aqui eu tenho uma lista com varios itens linha

      faturamento = 0
      # Excluir a 1º linha, porque tem um texto
      lista_texto = lista_texto[1:]# Aqui estou ignorando o indice 0, da lista e pegando do indice 1 ate o final
      #print(lista_texto)
      # Para cada linha do meu arquivo
      for linha in lista_texto:
        posicao_pv = linha.find(";")# methodo string. find dar a posição do ;
        valor = float (linha[posicao_pv + 1 : ])
        faturamento = faturamento + valor

      print(faturamento)
      
      with open("dados_de_venda.txt", "r") as arquivo:# Abrindo o arquivo porque quero ler no arquivo
            texto = arquivo.read() # ler o arquivo e armazenar dentro da variavel texto
            linhas = texto.split("\n") # method pega texto e separa cada item de acordo com (?) "enter"
            numero_linhas = len(linhas) # method len pega o tamanho da lista
            numero_colunas = len(linhas[0].split(";")) # method split pega o texto e separa cada item de acordo com (?) ";"
            print("Número de linhas:", numero_linhas) # printar o numero de linhas
            print("Número de colunas:", numero_colunas)# printar o numero de colunas

      
       

