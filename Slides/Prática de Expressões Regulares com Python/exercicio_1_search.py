#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#1. Código que retorne se um match pode ser encontrado ao se procurar pela palavra “sonhos”;

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retorna match object se caso a string for encontrada
x = re.search("sonhos", txt)

#saída de dados
if x:
    print("Match encontrado! A palavra 'sonhos' existe no texto.")
else:
    print("Nenhum match encontrado.")