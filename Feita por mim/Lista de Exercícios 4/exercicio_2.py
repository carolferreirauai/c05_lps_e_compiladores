#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#2.Código que retorne uma lista apenas das palavras que contém caracteres com acentos.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retornar a lista com acentos
x = re.findall("[a-zA-ZçÇ]*[ãÃéÉ][a-zA-ZçÇãÃéÉ]*", txt)

#saída de dados
print(x)