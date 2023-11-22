disciplina = "Data Science"
nota_final = 90
semestre = 2

if disciplina == "Data Science" and nota_final >= 80 and semestre !=1:
  print(f"Você foi aprovado em {disciplina} com media final {nota_final}")
else: 
  print(f"lamento, você não foi aprovado na disciplina {disciplina} pois sua media final ficou abaixo de 80")