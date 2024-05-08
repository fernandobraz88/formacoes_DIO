#METODOS

#.upper() => tudo em maiusculo
print('upper')
print("upper".upper())

#.lower() => tudo em minusculo
print("\nLOWER")
print("LOWER".lower())

#.title() => primeita letra em maiusculo
print('\ntitle')
print("title".title())

#.strip() => elimina os espaços em branco
print("\n  Strip  ")
print("  Strip  ".strip())

#.lstrip() => elimina os espaços em branco à esqueda
print("\n  lstrip   ")
print("  lstrip   ".lstrip())

#.rstrip() => elimina os espaços em branco à direita
print("\nrstrip   " + " oi")
print("rstrip   ".rstrip() + " oi")

#.center() => centraliza a string e insere caracteres pre definidos
print("\nCenter")
print("Center".center(12,"="))

#.join() => insere um caracter entre cada um dos caracteres da string
print("\nJoin")
print("-".join("Join"))

#print(f" ") => formata strings e variaveis para serem exibidas
pi = 3.14159
print(f'\no valor de pi é: {pi:.2f}\n') #:.nf =>casas decimais


#FATIAMENTO DE STRINGS 
#Toda String é um array de caracteres > utilizamos a indexação para retornar substrings
#todo array inicia com o indice [0]

nome = "Fernando Braz da Silveira"
print(nome[0]) #retorna caracter pelo indice
print(nome[:9]) #[:X] retona os caracteres do 0 até o X(excludente)
print(nome[9:]) #[X:] retorna os caracteres do X até o final
print(nome[9:14]) #[X:Y] retorna os caracteres entre X e Y
print(nome[0:14:2]) #[X:Y:Z] retorna os caracteres entre x e y a cada z posições
print(nome[::-1]) #[::-1] retorna a string de forma invertida

#STRINGS DE MULTIPLAS LINHAS
#os espaços e quebras de linahs sao exibidos
#escrever a string entre aspas triplas

mensagem = """
Mensagem 
    Generica
        Teste
        
"""
print(mensagem)