import numpy as np

def lerArq (inst):
  '''
    Essa função tem como objetivo ler as informações de arquivos em .txt
    Os arquivos lidos estarão na pasta 'datasets'
    O usuário deverá passar como parâmetro o nome da instância

    Após a leitura do arquivo, os dados (matrizes) serão armazenados em uma matriz do tipo numpy
  '''

  caminho = "C:/Users/edub_/OneDrive/Área de Trabalho/Grafos_Python/datasets/" + inst + ".txt" #definindo qual arquivo será utilizado
  with open(caminho, "r") as arq:    #abrindo arquivo para leitura
    dados = np.loadtxt(arq, dtype="int32")  #armazenando as informações em uma matriz de inteiros
    return dados  #retornando a matriz obtida pela leitura do arquivo


def escreverArq (matriz, inst):
  ''' 
    Essa função tem como objetivo mostrar na tela e salvar em um novo arquivo as informações obtidas da matriz 

    Como parâmetros são passados a matriz obtida após ler o arquivo e a instância fornecida pelo usuário (que indica o nome )
  '''

  print(f"{inst}.txt {matriz.shape[0]} {matriz.shape[1]}")  #printrando na tela as informações da matriz
   
  caminho_salvar = "C:/Users/edub_/OneDrive/Área de Trabalho/Grafos_Python/resultados_salvos/" + inst + "_resultadoSalvo.txt"  #definindo caminho/ nome onde será salva a matriz

  with open(caminho_salvar, "w") as salvar:  #abrindo o arquivo para salvar
    salvar.write(f"{inst}.txt {matriz.shape[0]} {matriz.shape[1]}")  #escrevendo o arquivo

