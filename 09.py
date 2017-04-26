print("Pressione 0 para sair!")
lista = []
num = 1
while(num != 0):
    num = int(input("Insira um número: "))
    lista.append(num)
soma = 0
for num in lista:
    soma += num
media = soma/len(lista)
print("{quant} números digitados, sua soma é {soma} e a média é {media:.2f}".format(
                                                                             quant=len(lista),
                                                                             soma=soma,
                                                                             media=media
                                                                             ))
