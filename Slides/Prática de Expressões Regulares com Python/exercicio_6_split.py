#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#6. Código que retorna uma lista de Strings que deverão ser quebradas toda vez que for encontrado no texto o caracter . (ponto) ou , (vírgula);

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#quebrar o texto quando tive . ou ,
x = re.split("\.|,", txt)

#saída de dados
print(x)