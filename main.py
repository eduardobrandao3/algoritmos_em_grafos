from manipulandoArquivos import manipArq

instancia = input("Informe a instancia do arquivo: ").strip() #recebendo o nome da instância e garantido que não tenha espaços extras

dados = manipArq.lerArq(instancia) #armazenando a matriz presente no arquivo atraves da função lerArq
manipArq.escreverArq(dados, instancia) #chamando a função escreverArq para printar na tela e salvar em arquivo 



