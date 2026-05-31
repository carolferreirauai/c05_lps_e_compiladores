#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#8. Código que responda quantas letras o texto base possui.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retorna as palavras
x = re.findall("[a-zA-ZçÇ]+", txt)

#saída de dados - tamanho da lista
print("quantidade: ", len(x))