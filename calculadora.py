n1 = float(input('Digite o primeiro número: '))
operador = input('escolha uma operação: +, -, * ou /: ')
n2 = float(input('Digite o segundo número: '))

if operador == '+':
 print (f'O RESULTADO É : {n1 + n2}')
if operador == '-':
 print(f'O RESULTADO É: {n1-n2 }')
if operador == '*': 
 print (f'O RESULTADO É: {n1*n2}')
if operador == '/':
 print(f'O RESULTADO É : {n1 % n2}') 
