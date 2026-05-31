#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#1.Código que substitua todas as palavras maiores que 5 caracteres por astericos (*).

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#substituir as palavras maiores que 6 por *
x = re.sub("[a-zA-zçÇãÃéÉ]{6,}","*", txt)

#saída de dados
print(x)