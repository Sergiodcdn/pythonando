# variável - int, float, string, bool
# ordem das operaçãoes = ** , * / // %, + -
# and e or, e not

idade = int(input('Digite a idade: '))
nome = input('Digite o nome: ')

def mostrar_tipo(n):
    print(type(n))

#print(type(idade))
mostrar_tipo(idade)

print(f'\nMeu nome é {nome} e tenho {idade} anos.')

letras = 0
for l in nome:
    letras += 1

if True:    
    print(f'\nO nome {nome} tem {letras} letas.\n')

if idade % letras == 0:
    pass
else:
    print('oxi não teve divisão perfeita')


c = 0
while c < letras:
    c += 1
    print(f'somando 1 ao c, que está com {c}')
    if c == letras:
        print('Acabo o while.')
    
for i in range(0, idade, 5):
    if i % 2 == 0:
        print(f'{i} pinchers')
        
#lista = .append, .pop,
notas = []
while True:
    nota_aluno = int(input('digite a nota, -1 para o código atual: '))
    if nota_aluno == -1:
        break
    notas.append(nota_aluno)
    
soma = 0
qtd = 0
for i in notas:
    soma += i
    qtd += 1
    
print(soma/qtd)

#dicionários = {chave: valor, chave2: valor2}

#função def fazer_resumo():
#   print()
#   return x
#   chego no return acaba função
#CRIAR MODULARIZAÇÃO PARA FUNÇÕES