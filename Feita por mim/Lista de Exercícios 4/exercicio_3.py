#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#3. Código que em um único REGEX, troque as letras maiúsculas por minúsculas, e vice-versa.

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#a regex busca qualquer letra. o segundo parâmetro pega o match (m) e inverte o tamanho usando a função nativa swapcase()
x = re.sub("[a-zA-ZçÇãÃéÉ]", lambda m: m.group().swapcase(), txt)

#saída de dados
print(x)