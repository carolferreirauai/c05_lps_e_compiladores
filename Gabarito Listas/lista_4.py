import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz."

# 1. Código que substitua todas as palavras maiores que 5 caracteres por astericos (*).
x = re.sub("[a-zA-zéÉçã]{5,}","*",txt)
print(x)

#2. Código que retorne uma lista apenas das palavras que contém caracteres com acentos.
for match in re.finditer("[A-Za-zç]*[éÉã]+[A-Za-zç]*",txt):
    print(match.group())

#3. Código que em um único REGEX, troque as letras maiúsculas por minúsculas, e vice-versa.
x = re.sub("[A-Za-zÀ-ÿ]", lambda m: m.group(0).swapcase(), txt)
print(x)

#4. Código que retorna a posição inicial e final da maior palavra do texto.
biggest_word_len = 0
biggest_word = " "

for match in re.finditer("[A-Za-zÀ-ÿ]+", txt):
    palavra = match.group()
    if len(palavra) >= biggest_word_len:
        biggest_word_len = len(palavra)
        biggest_word = palavra

x = re.search(biggest_word,txt)
print(x.span())

#5. Código que retorna uma lista apenas com as palavras que possuam de 2 a 6 letras.
for match in re.finditer(r"\b[A-Za-zÀ-ÿ]{2,6}\b", txt):
    print(match.group())

#6. Código que retorna uma lista de Strings que deverão ser quebradas toda vez que for encontrada uma letra maiúscula.
x = re.split("[A-ZÉ]",txt)
print(x)

#7. Código que retorne todas as palavras que contenham vogais.
for match in re.finditer("[A-Za-zÀ-ÿ]*[aeioué]+[A-Za-zÀ-ÿ]*", txt):
    print(match.group())

#8. Código que responda quantas letras o texto base possui.
contador = 0

for match in re.finditer("[A-Za-zÀ-ÿ]+", txt):
    contador += len(match.group())

print("Quantidade de letras: ", contador)