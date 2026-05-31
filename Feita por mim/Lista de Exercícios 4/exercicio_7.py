#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#7. Código que retorne todas as palavras que contenham vogais.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retorna as palavras que tem vogais
x = re.findall("[a-zA-ZçÇãÃéÉíÍ]*[aeiouAEIOUãÃéÉíÍ][a-zA-ZçÇãÃéÉíÍ]*", txt)

#saída de dados
print(x)