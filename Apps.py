import streamlit as st
import numpy as np

# Funktion zur Berechnung der Lagebeziehung mit Rechenweg und vollständiger Gauß-Elimination
def gauss_elimination(A, b):
    """Gauß-Elimination zur Lösung des Systems Ax = b"""
    n = len(b)
    M = np.hstack([A, b.reshape(-1, 1)])  # Augmentierte Matrix
    rechenweg = ""

    # Vorwärtssubstitution (Elimination)
    for i in range(n):
        # Pivotisierung: Zeilen tauschen, falls notwendig
        if M[i, i] == 0:
            for j in range(i+1, n):
                if M[j, i] != 0:
                    M[[i, j]] = M[[j, i]]
                    rechenweg += f"  Tausche Zeile {i+1} mit Zeile {j+1}, da der Pivot-Element von Zeile {i+1} null ist.\n"
                    break
        # Normiere die Zeile
        M[i] = M[i] / M[i, i]
        rechenweg += f"  Normiere Zeile {i+1} (Teile durch {M[i, i]}): {M[i]}\n"
        # Elimiere die Spalten unterhalb der Diagonalen
        for j in range(i + 1, n):
            M[j] -= M[j, i] * M[i]
            rechenweg += f"  Eliminiere Eintrag in Zeile {j+1}, Spalte {i+1}: {M[j]}\n"
    
    # Rückwärtssubstitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = M[i, -1] - np.dot(M[i, :-1], x)
        rechenweg += f"  Bestimme x_{i+1} = {M[i, -1]} - {np.dot(M[i, :-1], x)} = {x[i]}\n"
    return x, rechenweg

def check_lagebeziehung(a1, b1, a2, b2):
    a1, b1, a2, b2 = np.array(a1), np.array(b1), np.array(a2), np.array(b2)
    rechenweg = ""

    # Schritt 1: Die Gleichungen der beiden Geraden
    rechenweg += "1️⃣ **Gleichungen der beiden Geraden:**\n"
    rechenweg += f"   Gerade 1: r₁(t) = {a1} + t * {b1} \n"
    rechenweg += f"   Gerade 2: r₂(s) = {a2} + s * {b2} \n\n"

    # Schritt 2: Überprüfung auf Parallelität
    rechenweg += "2️⃣ **Überprüfung auf Parallelität:**\n"
    if np.linalg.matrix_rank(np.column_stack((b1, b2))) == 1:
        rechenweg += "   Die Richtungsvektoren b₁ und b₂ sind linear abhängig.\n"
        rechenweg += "   Die Geraden sind **parallel**.\n"
        
        if np.linalg.matrix_rank(np.column_stack((b1, a2 - a1))) == 1:
            rechenweg += "   Die Geraden sind **identisch**.\n"
            return "Die Geraden sind **identisch**.", rechenweg
        else:
            rechenweg += "   Die Geraden sind **parallel**, aber nicht identisch.\n"
            return "Die Geraden sind **parallel**, aber nicht identisch.", rechenweg

    rechenweg += "   Die Richtungsvektoren sind **linear unabhängig**.\n"
    rechenweg += "   Die Geraden sind **nicht parallel**.\n\n"

    # Schritt 3: Überprüfung auf Schnittpunkt
    rechenweg += "3️⃣ **Überprüfung auf Schnittpunkt:**\n"
    rechenweg += "   r₁(t) = r₂(s) → a₁ + t * b₁ = a₂ + s * b₂\n"
    rechenweg += "   → t * b₁ - s * b₂ = a₂ - a₁\n"
    rechenweg += "   Dies ergibt das lineare Gleichungssystem:\n"

    A = np.column_stack((b1, -b2))
    b = a2 - a1

    rechenweg += f"   Die augmentierte Matrix lautet:\n"
    rechenweg += f"   [ [{b1[0]}, {-b2[0]}], \n"
    rechenweg += f"     [{b1[1]}, {-b2[1]}], \n"
    rechenweg += f"     [{b1[2]}, {-b2[2]}] ]\n"
    rechenweg += f"   Rechter Vektor: [{b[0]}, {b[1]}, {b[2]}]\n\n"

    # Lösung mit Gauß-Verfahren
    try:
        lambdas, step_rechenweg = gauss_elimination(A, b)
        schnittpunkt = a1 + lambdas[0] * b1

        rechenweg += step_rechenweg  # Detaillierte Schritte der Gauß-Elimination
        rechenweg += f"   λ₁ = {lambdas[0]} \n   λ₂ = {lambdas[1]}\n"
        rechenweg += f"   Der Schnittpunkt der beiden Geraden ist: {schnittpunkt}\n"
        
        return f"Die Geraden schneiden sich in {schnittpunkt}.", rechenweg

    except Exception as e:
        rechenweg += "   Es gibt keinen Schnittpunkt. Die Geraden sind **windschief**.\n"
        return "Die Geraden sind **windschief**.", rechenweg

# Streamlit UI
st.title("Lagebeziehung von zwei Geraden mit Stütz- und Richtungsvektoren")

st.write("Gib die Stütz- und Richtungsvektoren der beiden Geraden ein (z. B. `(1,2,3)` für Stützvektor und `(4,5,6)` für Richtungsvektor).")

# Eingabefelder für Vektoren
a1 = st.text_input("Stützvektor der 1. Gerade (z. B. (1,2,3))", "(0,0,0)")
b1 = st.text_input("Richtungsvektor der 1. Gerade (z. B. (4,5,6))", "(1,1,1)")

a2 = st.text_input("Stützvektor der 2. Gerade (z. B. (7,8,9))", "(1,1,1)")
b2 = st.text_input("Richtungsvektor der 2. Gerade (z. B. (10,11,12))", "(1,-1,1)")

if st.button("Berechnen"):
    try:
        # Konvertiere die Eingabe in Vektoren
        a1 = np.array(eval(a1))
        b1 = np.array(eval(b1))
        a2 = np.array(eval(a2))
        b2 = np.array(eval(b2))

        result, rechenweg = check_lagebeziehung(a1, b1, a2, b2)
        st.success(result)
        st.markdown(rechenweg)

    except Exception as e:
        st.error(f"Fehler bei der Eingabe: {e}")
