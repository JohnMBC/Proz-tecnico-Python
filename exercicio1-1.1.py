# Referenciando um arquivo com caminhos diferentes
arquivo_ref1 = open ("exercicio2.py") # Caminho relativo
print(arquivo_ref1.read()) # Printar o conteudo do arquivo
arquivo_ref2 = open ("C:\\Users\\johnn\\Desktop\\projeto-MEI\\psdeucodigo\\arquivo.txt") # Caminho absoluto

import os
caminho_arquivo = "C:\\Users\\johnn\\Desktop\\projeto-MEI\\psdeucodigo\\arquivo.txt"
if os.path.exists(caminho_arquivo): # Verifica se o arquivo existe no caminho especificado 
    if os.access(caminho_arquivo, os.R_OK): # Verifica se o arquivo tem permissão de leitura  
        with open(caminho_arquivo) as arquivo_ref2: # Abrindo o arquivo porque quero ler no arquivo         
            conteudo = arquivo_ref2.read() # Ler o arquivo e armazenar dentro da variavel conteudo 
            print(conteudo) # Printar o conteudo do arquivo 
    else:
        print("Sem permissão para ler o arquivo.")# Printar mensagem de erro
 
    

