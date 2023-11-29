asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}
for asignatura in asignaturas:
    nota = float(input("Introduce la nota de "+ asignatura))
    notas[asignatura] = nota

print("Notas")
for asignatura, nota in notas.items():
    print(asignatura +" = "+ str(nota))