# Exercicio 21


notas = {
  "português": "10",
  "matemática": "6",
  "física": "7",
  "história": "8",
  "geografia": "9",
  "biologia": "5"
}

materia = input("Digite o nome da matéria: ")

if materia in notas:
  nota = notas[materia]
  print(f"A nota de {materia} é {nota}.")
else:
  print("Matéria não encontrada!")


# fim