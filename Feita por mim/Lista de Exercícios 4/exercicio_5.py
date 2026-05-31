#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#5. Código que retorna uma lista apenas com as palavras que possuam de 2 a 6 letras.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retornar lista das palavras com 2 a 6 letras
#os \b garantem que a palavra comece e termine ali, isolando-a.
x = re.findall(r"\b[a-zA-ZçÇãÃéÉ]{2,6}\b", txt)

#saída de dados
print(x)