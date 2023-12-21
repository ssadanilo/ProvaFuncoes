# Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
# Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. 
# Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: 
# "Reprovado" se a média for menor que 7, 
# "Aprovado" se a média for maior ou igual a 7, 
# e "Parabéns, sua média é 10" se a média for igual a 10.


# Dicionário criado em colchetes, para permitir que a lista comece vazia

notas = []

# Nesse input o cliente escolhe quantas notas deseja incluir

qto_notas = int(input('Quantas notas do aluno serão acrescentadas?: ')) 

# Criado laço for, para incluir a quantidade de inputs desejada acima

for i in range(qto_notas):
    nota = (float(input(f'Digite a nota {i+1}: ')))
    notas.append(nota)

# Função para calcular a média das notas

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

media_notas = calcular_media(notas) # Criada a variável para guardar média das notas
print(calcular_media(notas))

# Função que verifica a aprovação ou reprovação do aluno

def verificar_situacao(media):
    if media < 7:
        print(f"Sua nota média é {media_notas} e você está Reprovado!")
    elif media >= 7 and media < 10:
        print(f"Sua nota média é {media_notas} e você está Aprovado!")
    elif media == 10:
        print(f"Sua nota média é {media_notas} e você está de Parabéns!")

verificar_situacao(media_notas) # Finaliza a verificação da média do aluno