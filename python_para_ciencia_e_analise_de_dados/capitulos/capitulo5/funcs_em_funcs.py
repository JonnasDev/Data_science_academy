import math

def func_numPrimo(num):
  if (num % 2) == 0 and nun > 2:
    return "Este numero não é primo"
  
  for i in range(3, int(math.sqrt(num)) + 1,2):
    if(num % i) == 0:
      return("Este numero não é primo")
    
  return "Este numero é  primo"

func_numPrimo(541)
func_numPrimo(813)  