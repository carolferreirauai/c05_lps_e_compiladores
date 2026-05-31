#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#6. Código que retorna uma lista de Strings que deverão ser quebradas toda vez que for encontrada uma letra maiúscula.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retorna a lista aonde vai ser quebrada
x = re.split("[A-ZÇÉ]+", txt)

#saída de dados
print(x)