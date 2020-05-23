rows = []

# le o arquivo e retira o breakline
with open('textos.txt', 'r') as fileText:
    for row in fileText:
        # adiciona a linha ao array
        rows.append(row.rstrip('\n'))

# se tiver linhas imprime na tela
if len(rows) >= 1:
    text = ',\n'.join(rows)[0:-2]
    print(text)
else:
    print("arquivo está vázio")
