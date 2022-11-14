def encode(palavra1, chave1):
    palavra1 = palavra1.upper()
    chave1 = chave1.upper()
    lista = []
    palavra = []
    chave = []
    chave_num = []

    palavra[:0] = palavra1
    chave[:0] = chave1

    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z']
    dic = {}

    # POPULANDO O DICIONARIO
    j=0
    for i in lista:
        dic[j] = lista[j]
        j += 1

    # DEIXANDO A CHAVE DO MESMO TAMANHO DA PALAVRA
    while len(chave) != len(palavra):
        if len(chave) < len(palavra):
            dif = len(palavra) - len(chave)
            for i in range(dif):
                chave.append(chave[i])
        else:
            dif = len(chave) - len(palavra)
            for i in range(dif):
                ult = len(chave) - 1
                chave.remove(chave[ult])  

    # ACHANDO NUMERO DAS CHAVES
    c1, c2 = 0, 0
    while len(chave_num) < len(chave):
        if dic[c1] == chave[c2]:
            chave_num.append(c1)
            c2 += 1
            c1 = 0
        else:
            c1 += 1

    resposta = []

    c1, c2, c3 = 0, 0, 0
    while len(resposta) < len(palavra1):
        if dic[c1] == palavra[c2]:
            x = c1 + chave_num[c3]
            if x > 25:
                x = x - 26
            resposta.append(dic[x])
            c1 = 0
            c2 += 1
            c3 += 1
        else:
            c1 += 1

    str_resposta=''.join(resposta)
    return str_resposta


palavra = input('\nDigite uma palavra: ')
chave = input('Digite uma chave: ')

print('\nRespsota:',encode(palavra, chave))


