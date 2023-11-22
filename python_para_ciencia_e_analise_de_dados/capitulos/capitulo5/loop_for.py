matriz = [[42,23,44], [231,233,544], [824,924,234]]
maiorNumero = 0

for linha in matriz:
  for num in linha:
    if num > maiorNumero:
      maiorNumero = num
print("Maior numero: ", maiorNumero)      