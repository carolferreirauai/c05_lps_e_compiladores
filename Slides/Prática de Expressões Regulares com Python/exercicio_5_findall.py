#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#5. Código que retorna uma lista apenas com as palavras que possuam 9 letras ou mais;

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#procura palavras com mais de 9 ou mais letras, retorna uma lista.
x = re.findall("[a-zA-ZçÇãÃ]{9,}", txt)

#saída de dados
print(x)