primos = []

for num in range (2,31):
  ehPrimo = True
  
  i = 2
  while i <= num // 2:
      if num % i == 0:
         ehPrimo = False
         break
      i += 1
if ehPrimo:
  primos.append(num)
  
print(primos)    
  
    