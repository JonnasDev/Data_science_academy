varGlobal = 10 # Variavel global

def func_multiplicaNumeros(num1, num2):
  varLocal = num1 * num2 # Variavel local
  print(f"Aqui esta a varivael local",varLocal)

func_multiplicaNumeros(5, 19)  

print(f"Aqui esta a varivael global", varGlobal)