#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#4. Código que retorna a posição inicial e final da maior palavra do texto.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retornar a todas palavras
x = re.finditer("[a-zA-ZçÇãÃéÉ]+", txt)

#encontra o maior match baseando-se no tamanho (len) do texto capturado (.group())
maior = max(x, key=lambda m: len(m.group()))

#saída de dados - retorna a palavra e a tupla contendo a posição inicial e final
print("A maior palavra é", maior.group())
print("Posição:", maior.span())