#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#2. Código que retorne uma lista apenas das palavras terminadas com “as”; 
# (Atenção, a classe de caracteres [a-zA-Z] naturalmente não aceita caracteres da língua portuguesa, por isso, você deve adicioná-los manualmente dentro da classe. Ex: [a-zA-Zç]

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#retorna uma lista contendo todos os padrões identificados dentro do texto
x = re.findall("[a-zA-zç]+as", txt)

#saída de dados
print(x)