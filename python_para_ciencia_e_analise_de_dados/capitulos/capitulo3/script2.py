print ('Bem-vindo a calculadora do curso')

num1 = float(input("Insira o numero 1: "))
num2 = float(input("Insira o numero 2: "))

operacao = input("Selecione uma operação: [+, -, *, /]: ")

if operacao == "+":
  resultado = num1 + num2
  print ("O resultado é: ", resultado)
  
elif operacao == "-":
  resultado = num1 - num2
  print ("O resultado é: ", resultado) 

elif operacao == "*":
  resultado = num1 * num2
  print ("O resultado é: ", resultado)
  
elif operacao == "/":
  resultado = num1 / num2
  print ("O resultado é: ", resultado)
  
else:
  print("Não foi possivel realizar o calculo, o sinal da operação esta incorreto")       