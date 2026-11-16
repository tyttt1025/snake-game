import random
elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]

while len(elements) > 0:
    selected = elements[random.randint(0, len(elements) - 1)]
    input (f"Valency of {selected}: ")
    elements.remove(selected)