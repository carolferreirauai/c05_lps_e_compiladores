#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#4. Código que retorna a posição inicial e final da palavra “inspiração” dentro do texto;

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#procura a palavra inspiração no texto
x = re.search("inspiração", txt)

#saída de dados
print(x.span())