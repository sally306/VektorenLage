import numpy as np

def lagebeziehung_geraden(A, v1, B, v2):
    # Prüfe auf Parallelität (Richtungsvektoren sind linear abhängig)
    if np.cross(v1, v2).tolist() == [0, 0, 0]:
        # Prüfe, ob die Geraden identisch sind (B-A muss ein Vielfaches von v1 sein)
        if np.linalg.matrix_rank(np.column_stack([v1, B - A])) == 1:
            return "Die Geraden sind identisch."
        return "Die Geraden sind parallel, aber verschieden."

    # LGS aufstellen zur Schnittpunktprüfung: A + t*v1 = B + s*v2
    M = np.column_stack([v1, -v2])
    try:
        t_s = np.linalg.solve(M, B - A)
        schnittpunkt = A + t_s[0] * v1
        return f"Die Geraden schneiden sich im Punkt {schnittpunkt}."
    except np.linalg.LinAlgError:
        return "Die Geraden sind windschief."

# Beispiel:
A = np.array([1, 2, 3])
v1 = np.array([1, 1, 1])
B = np.array([2, 3, 4])
v2 = np.array([1, -1, 2])

print(lagebeziehung_geraden(A, v1, B, v2))
