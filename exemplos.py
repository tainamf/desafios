#MANIPULAÇAO DE LISTAS
lista = [1, 2, 3, 4, 5]
print(lista)
print('o terceiro numero da lista é:', lista[2] ) #mostrar um elemento da lista (toda lista cmç pelo 0)
lista.append(10) #add um elemento novo
print(lista)
lista.remove(1) #remover algo da lista
print(lista)
lista.reverse() #muda a ordem
print(lista)

print('-----------------------')

#REPETIÇÕES (FOR E WHILE)
for n in range(1,11): #for: usado quando já sabemos quantas vezes queremos repetir algo
 print(n)

print('----------------')

m = 1
while m <= 10:  #while: repete um bloco de código enquanto uma condição for verdadeira (m menor que 10)
 print (m)
 #se parar aqui vai repetir o 1 pra sempre (experiencia propria KKKKKKKKKKKKKKKKKKKKKKKKKKK)
 m += 1 #Incrementa o número para não entrar em loop infinito, quando numero chegar no 11 a condição será falsa e o loop para

print('tabuada de x')
numero = int(input('digite o numero: '))
for i in range(1,11):
 print(f'{numero} x {i} = {numero * i}') 

print ('---------------------')

#CONDICIONAIS
idd = int(input('qual sua idade? '))
if idd > 17:
 print('você é de maior')
else:
 print ('você é de menor')

print('--------------------')
n1 = int(input('digite o 1º número: '))
n2 = int(input('digite o 2º numero: '))
if n1 > n2:
 print(f'{n1} é maior que {n2}')
elif n1 < n2 :
 print(f'{n1} é menor que {n2}')
else:
 print(f'{n1} e {n2} são iguais')

print('----------------------------')

#FUNÇOES
# função que recebe um número e retorna o dobro dele
def dobro(num): 
 return num * 2 #multiplicar por 2
num = int(input('digite um numero: '))
print('o dobro é: ', dobro(num))
print('--------------------')
# função que recebe uma lista de números e retorna a soma deles
def somar(lista):
 return sum(lista) #sum: soma tudo que ta na lista
nume = [1,2,2,3,5]
print(f'lista: {nume}')
print('a soma da lista é:', somar(nume))
print('--------------------')
#função que recebe um nome e recebe um bem vindo
def bv(nome):
 print(f'Olá {nome} bem vindo(a)!')
nomeu = input('qual seu nome? ')
bv(nomeu)

print('------------------------')

#strings
nome = str(input('qual seu nome?'))
print('nome ao contrario: ', nome[::-1]) #[::-1]: inverte str

#Solicite uma frase e conte quantas vogais existem nela
def contav(frase): #percorre a frase e soma as vogais
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in frase if letra in vogais) #Conta as letras que são vogais
    return contador

frase = input("Digite uma frase: ")
print("Número de vogais:", contav(frase))

#todas as letras para maiúsculas
nomem = input("Digite seu nome: ")
print("Nome em maiúsculas:", nomem.upper()) #upper(): deixa tudo maiusculo