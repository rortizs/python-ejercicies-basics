"""Cuadernillo 0 - Tema 13: Listas: crear, append(), recorrer, len() y count()."""

prioridades = []
prioridades.append("ALTA")
prioridades.append("BAJA")
prioridades.append("ALTA")
print(f"Total: {len(prioridades)}, en ALTA: {prioridades.count('ALTA')}")
for p in prioridades:
    print(p)
