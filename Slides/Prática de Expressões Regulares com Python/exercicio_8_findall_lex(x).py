#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#8. Código que responda quantas palavras o texto base possui.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retornar o texto
x = re.findall("[a-zA-ZçÇãÃéÉ]+", txt)

#saída de dados, quantidades de palavras.
print("quantidade: ", len(x)) #pega o tamanho da lista