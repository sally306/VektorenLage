import streamlit as st
import numpy as np

# Funktion zur Berechnung der Lagebeziehung mit detailliertem Rechenweg
def check_lagebeziehung(a1, b1, a2, b2):
    a1, b1, a2, b2 = np.array(a1), np.array(b1), np.array(a2), np.array(b2)
    rechenweg = "**Detaillierter Rechenweg:**\n\n"

    # Schritt 1: Die Gleichungen der beiden Geraden
    rechenweg += f"1️⃣ Die beiden Geraden lassen sich wie folgt beschreiben:\n"
    rechenweg += f"   Gerade 1: r₁(t) = {a1} + t * {b1}\n"
    rechenweg += f"   Gerade 2: r₂(s) = {a2} + s * {b2}\n\n"

    # Schritt 2: Überprüfung auf Parallelität
    rechenweg += "2️⃣ Überprüfung, ob die Geraden parallel sind:\n"
    rechenweg += "Die Richtungsvektoren müssen **linear abhängig** sein, damit die Geraden parallel sind.\n"
    
    if np.linalg.matrix_rank(np.column_stack((b1, b2))) == 1:
        rechenweg += "   Da die Richtungsvektoren **linear abhängig** sind, sind die Geraden **parallel**.\n"
        
        # Überprüfung, ob die Geraden identisch sind
        if np.linalg.matrix_rank(np.column_stack((b1, a2 - a1))) == 1:
            return "Die Geraden sind **identisch**.", rechenweg
        
        return "Die Geraden sind **parallel**, aber nicht identisch.", rechenweg

    rechenweg += "   Da die Richtungsvektoren **linear unabhängig** sind, sind die Geraden **nicht parallel**.\n\n"

    # Schritt 3: Überprüfung auf Schnittpunkt
    rechenweg += "3️⃣ Überprüfung, ob die Geraden sich schneiden:\n"
    rechenweg += "Um zu überprüfen, ob sich die Geraden schneiden, lösen wir das lineare Gleichungssystem:\n"
    rechenweg += "   a1 + t * b1 = a2 + s * b2\n"
    rechenweg += "   Umgestellt ergibt sich das System:\n"
    rechenweg += f"   {b1} * t - {b2} * s = {a2} - {a1}\n"
    
    A = np.column_stack((b1, -b2))
    
    try:
        # Lösen des linearen Gleichungssystems für den Schnittpunkt
        lambdas = np.linalg.solve(A, a2 - a1)
        schnittpunkt = a1 + lambdas[0] * b1
        
        rechenweg += "   Wir lösen das lineare Gleichungssystem und erhalten:\n"
        rechenweg += f"   λ₁ = {lambdas[0]} \n   λ₂ = {lambdas[1]}\n"
        rechenweg += f"   Der Schnittpunkt der beiden Geraden ist: {schnittpunkt}\n"
        rechenweg += "Die Geraden schneiden sich, und der Schnittpunkt ist somit der Punkt " + str(schnittpunkt) + ".\n"
        return f"Die Geraden schneiden sich in {schnittpunkt}.", rechenweg

    except np.linalg.LinAlgError:
        rechenweg += "   Das lineare Gleichungssystem hat keine Lösung. Die Geraden sind **windschief**.\n"
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
