#Texto Base:Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz
#3. Código que em um único REGEX, troque as palavras “maior” e “grande” pela palavra “surreal” e mostre a nova frase após as trocas;

#biblioteca
import re

#texto para realizar o teste
txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#substitui o maior por grande
x = re.sub("maior|grande", "surreal", txt)

#saída de dados
print(x)