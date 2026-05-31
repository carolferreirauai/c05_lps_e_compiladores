#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#7. Código que retorne todas as palavras que possuam a letra “é” (com acento) seja em maiúscula ou minúscula;

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#lista de palavra com é
x = re.findall("[a-zA-ZçÇ]*[éÉ][a-zA-ZçÇ]*", txt)

#saída de dados
print(x)