import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Ausführliche Analyse")

# Beschreibung
st.write("""
Geben Sie die Stütz- und Richtungsvektoren für zwei Geraden im ℝ³ ein. 
Wir untersuchen ihre Lagebeziehung (parallel, schneidend, windschief, identisch) 
und berechnen bei sich schneidenden Geraden den Schnittpunkt.
Die Schritte sind detailliert und nachvollziehbar.
""")

# Eingabefelder für die erste Gerade
st.header("Gerade 1")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Stützvektor g1")
    x1 = st.number_input("x1", value=0.0, step=1.0, key="x1")
    y1 = st.number_input("y1", value=0.0, step=1.0, key="y1")
    z1 = st.number_input("z1", value=0.0, step=1.0, key="z1")

with col2:
    st.subheader("Richtungsvektor r1")
    rx1 = st.number_input("rx1", value=1.0, step=1.0, key="rx1")
    ry1 = st.number_input("ry1", value=2.0, step=1.0, key="ry1")
    rz1 = st.number_input("rz1", value=3.0, step=1.0, key="rz1")

# Eingabefelder für die zweite Gerade
st.header("Gerade 2")
col3, col4 = st.columns(2)

with col3:
    st.subheader("Stützvektor g2")
    x2 = st.number_input("x2", value=1.0, step=1.0, key="x2")
    y2 = st.number_input("y2", value=1.0, step=1.0, key="y2")
    z2 = st.number_input("z2", value=1.0, step=1.0, key="z2")

with col4:
    st.subheader("Richtungsvektor r2")
    rx2 = st.number_input("rx2", value=4.0, step=1.0, key="rx2")
    ry2 = st.number_input("ry2", value=5.0, step=1.0, key="ry2")
    rz2 = st.number_input("rz2", value=6.0, step=1.0, key="rz2")

# Vektoren als Listen definieren
g1 = [x1, y1, z1]
r1 = [rx1, ry1, rz1]
g2 = [x2, y2, z2]
r2 = [rx2, ry2, rz2]

# Funktion für Vektorsubtraktion
def vector_subtract(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

# Berechnungen durchführen
if st.button("Lagebeziehung berechnen"):
    st.header("Schritt-für-Schritt-Analyse")

    # Schritt 1: Geradengleichungen aufstellen
    st.subheader("Schritt 1: Geradengleichungen aufstellen")
    st.write("Die parametrische Form einer Geraden ist: **x = g + t * r**.")
    st.write("**Gerade 1:**")
    st.write(f"g1 = {g1}, r1 = {r1}")
    st.write(f"x = {g1[0]} + t * {r1[0]}")
    st.write(f"y = {g1[1]} + t * {r1[1]}")
    st.write(f"z = {g1[2]} + t * {r1[2]}")
    st.write("**Gerade 2:**")
    st.write(f"g2 = {g2}, r2 = {r2}")
    st.write(f"x = {g2[0]} + s * {r2[0]}")
    st.write(f"y = {g2[1]} + s * {r2[1]}")
    st.write(f"z = {g2[2]} + s * {r2[2]}")

    # Schritt 2: Prüfung auf Kollinearität der Richtungsvektoren
    st.subheader("Schritt 2: Prüfen, ob die Geraden parallel oder identisch sind")
    st.write("Zwei Geraden sind parallel oder identisch, wenn ihre Richtungsvektoren kollinear sind, d.h. r2 = λ * r1.")
    st.write(f"r1 = {r1}, r2 = {r2}")
    
    collinear = True
    lambda_values = []
    for i in range(3):
        if r1[i] != 0 and r2[i] != 0:
            lambda_val = r2[i] / r1[i]
            lambda_values.append(lambda_val)
            st.write(f"Komponente {i+1}: {r2[i]} / {r1[i]} = {lambda_val}")
        elif r1[i] == 0 and r2[i] == 0:
            st.write(f"Komponente {i+1}: Beide 0, passt.")
        else:
            st.write(f"Komponente {i+1}: r1[{i}] = {r1[i]}, r2[{i}] = {r2[i]} → kein Vielfaches!")
            collinear = False
            break
    
    if collinear and lambda_values:
        first_lambda = lambda_values[0]
        for lam in lambda_values[1:]:
            if abs(lam - first_lambda) > 1e-6:
                collinear = False
                st.write(f"λ-Werte unterschiedlich: {lambda_values} → keine Vielfachen!")
                break
        if collinear:
            st.write(f"Die Richtungsvektoren sind kollinear (λ = {first_lambda}), also sind die Geraden parallel oder identisch.")
            
            # Schritt 2.1: Prüfung, ob Stützpunkt g2 auf Gerade 1 liegt
            st.subheader("Schritt 2.1: Prüfen, ob die Geraden identisch sind")
            st.write("Da die Geraden kollinear sind, prüfen wir, ob sie identisch sind.")
            st.write("Dazu prüfen wir, ob der Stützvektor g2 auf Gerade 1 liegt: g2 = g1 + t * r1.")
            diff = vector_subtract(g2, g1)
            st.write(f"g2 - g1 = {g2} - {g1}")
            st.write(f"        = [{g2[0]} - ({g1[0]}), {g2[1]} - ({g1[1]}), {g2[2]} - ({g1[2]})]")
            st.write(f"        = {diff}")
            
            st.write("Nun prüfen wir, ob g2 - g1 ein Vielfaches von r1 ist:")
            t_values = []
            for i in range(3):
                if r1[i] != 0:
                    t_val = diff[i] / r1[i]
                    t_values.append(t_val)
                    st.write(f"Komponente {i+1}: {diff[i]} / {r1[i]} = {t_val}")
                elif diff[i] == 0:
                    st.write(f"Komponente {i+1}: Beide 0, passt.")
                else:
                    st.write(f"Komponente {i+1}: r1[{i}] = 0, diff[{i}] = {diff[i]} ≠ 0 → kein Vielfaches!")
                    t_values = []
                    break
            
            if t_values:
                first_t = t_values[0]
                identical = True
                for t_val in t_values[1:]:
                    if abs(t_val - first_t) > 1e-6:
                        identical = False
                        st.write(f"t-Werte unterschiedlich: {t_values} → Die Geraden sind nicht identisch!")
                        break
                if identical:
                    st.write(f"Alle t-Werte sind gleich (t = {first_t}), die Geraden sind identisch!")
                    st.write("Da die Geraden identisch sind, haben sie unendlich viele Schnittpunkte.")
                else:
                    st.write("Die Geraden sind echt parallel (kein Schnittpunkt).")
            else:
                st.write("Die Geraden sind echt parallel (kein Schnittpunkt).")
    else:
        st.write("Die Richtungsvektoren sind nicht kollinear, also sind die Geraden entweder schneidend oder windschief.")
        
        # Schritt 3: Gleichungssystem aufstellen und durch Substitution lösen
        st.subheader("Schritt 3: Gleichungssystem aufstellen")
        st.write("Da die Geraden nicht kollinear sind, prüfen wir, ob sie sich schneiden.")
        st.write("Wir setzen die Geradengleichungen gleich:")
        st.write(f"I.   {g1[0]} + t * {r1[0]} = {g2[0]} + s * {r2[0]}")
        st.write(f"II.  {g1[1]} + t * {r1[1]} = {g2[1]} + s * {r2[1]}")
        st.write(f"III. {g1[2]} + t * {r1[2]} = {g2[2]} + s * {r2[2]}")
        
        st.write("Umstellen der Gleichungen:")
        eq1 = f"{r1[0]} * t - {r2[0]} * s = {g2[0]} - {g1[0]}"
        eq2 = f"{r1[1]} * t - {r2[1]} * s = {g2[1]} - {g1[1]}"
        eq3 = f"{r1[2]} * t - {r2[2]} * s = {g2[2]} - {g1[2]}"
        st.write(f"I.   {eq1}")
        st.write(f"II.  {eq2}")
        st.write(f"III. {eq3}")
        
        # Koeffizienten und Konstanten definieren
        a1, b1, c1 = r1[0], -r2[0], g2[0] - g1[0]
        a2, b2, c2 = r1[1], -r2[1], g2[1] - g1[1]
        a3, b3, c3 = r1[2], -r2[2], g2[2] - g1[2]
        
        # Schritt 4: Substitution
        st.subheader("Schritt 4: Gleichungssystem durch Substitution lösen")
        st.write("Wir lösen das Gleichungssystem, indem wir t aus Gleichung I ausdrücken und in die anderen Gleichungen einsetzen.")
        
        # t aus Gleichung I ausdrücken
        if a1 != 0:
            st.write(f"Gleichung I: {a1} * t - {b1} * s = {c1}")
            st.write(f"Umstellen nach t: {a1} * t = {c1} + {b1} * s")
            st.write(f"t = ({c1} + {b1} * s) / {a1}")
            t_expr = f"({c1} + {b1} * s) / {a1}"
            t_val = lambda s: (c1 + b1 * s) / a1
        else:
            st.write("Der Koeffizient von t in Gleichung I ist 0, wir versuchen eine andere Gleichung.")
            st.stop()
        
        # t in Gleichung II einsetzen
        st.write(f"Setze t = {t_expr} in Gleichung II ein:")
        st.write(f"Gleichung II: {a2} * t - {b2} * s = {c2}")
        st.write(f"Einsetzen: {a2} * ({t_expr}) - {b2} * s = {c2}")
        st.write(f"Multiplizieren: ({a2} * ({c1} + {b1} * s)) / {a1} - {b2} * s = {c2}")
        st.write(f"Umstellen: ({a2} * {c1} + {a2} * {b1} * s) / {a1} - {b2} * s = {c2}")
        st.write(f"Multiplizieren mit {a1}, um den Nenner zu beseitigen:")
        st.write(f"{a2} * {c1} + {a2} * {b1} * s - {b2} * s * {a1} = {c2} * {a1}")
        st.write(f"Umstellen nach s: {a2} * {b1} * s - {b2} * {a1} * s = {c2} * {a1} - {a2} * {c1}")
        st.write(f"s * ({a2} * {b1} - {b2} * {a1}) = {c2} * {a1} - {a2} * {c1}")
        coeff_s = a2 * b1 - b2 * a1
        const_s = c2 * a1 - a2 * c1
        st.write(f"s * {coeff_s} = {const_s}")
        
        if coeff_s != 0:
            s = const_s / coeff_s
            st.write(f"s = {const_s} / {coeff_s} = {s:.6f}")
        else:
            st.write("Der Koeffizient von s ist 0, das System ist nicht eindeutig lösbar.")
            if const_s == 0:
                st.write("0 = 0, das System hat unendlich viele Lösungen. Die Geraden liegen in einer Ebene.")
            else:
                st.write(f"0 = {const_s}, ein Widerspruch. Die Geraden sind windschief.")
            st.stop()
        
        # t berechnen
        t = t_val(s)
        st.write(f"Setze s = {s:.6f} in t ein:")
        st.write(f"t = ({c1} + {b1} * {s:.6f}) / {a1}")
        st.write(f"t = {t:.6f}")
        
        # Schritt 5: Konsistenzprüfung mit Gleichung III
        st.subheader("Schritt 5: Konsistenzprüfung mit Gleichung III")
        st.write("Wir setzen t und s in Gleichung III ein, um die Konsistenz zu prüfen:")
        st.write(f"Gleichung III: {a3} * t - {b3} * s = {c3}")
        st.write(f"Einsetzen: {a3} * {t:.6f} - {b3} * {s:.6f}")
        left_side = a3 * t - b3 * s
        st.write(f"Linke Seite: {left_side:.6f}")
        st.write(f"Rechte Seite: {c3}")
        if abs(left_side - c3) < 1e-6:
            st.write("Die Gleichung ist erfüllt (innerhalb der Toleranz), das System ist lösbar.")
        else:
            st.write("Die Gleichung ist nicht erfüllt, das System hat keine Lösung. Die Geraden sind windschief.")
            st.stop()
        
        # Schritt 6: Schnittpunkt berechnen
        st.subheader("Schritt 6: Schnittpunkt berechnen")
        st.write("Da das System lösbar ist, berechnen wir den Schnittpunkt mit t in Gerade 1:")
        x = g1[0] + t * r1[0]
        y = g1[1] + t * r1[1]
        z = g1[2] + t * r1[2]
        st.write(f"x = {g1[0]} + {t:.6f} * {r1[0]} = {x:.6f}")
        st.write(f"y = {g1[1]} + {t:.6f} * {r1[1]} = {y:.6f}")
        st.write(f"z = {g1[2]} + {t:.6f} * {r1[2]} = {z:.6f}")
        schnittpunkt = [x, y, z]
        st.write(f"Schnittpunkt (Gerade 1): {schnittpunkt}")

        # Überprüfung mit Gerade 2
        st.write("Überprüfung mit s in Gerade 2:")
        x2_check = g2[0] + s * r2[0]
        y2_check = g2[1] + s * r2[1]
        z2_check = g2[2] + s * r2[2]
        st.write(f"x = {g2[0]} + {s:.6f} * {r2[0]} = {x2_check:.6f}")
        st.write(f"y = {g2[1]} + {s:.6f} * {r2[1]} = {y2_check:.6f}")
        st.write(f"z = {g2[2]} + {s:.6f} * {r2[2]} = {z2_check:.6f}")
        schnittpunkt2 = [x2_check, y2_check, z2_check]
        st.write(f"Schnittpunkt (Gerade 2): {schnittpunkt2}")

        # Endgültiges Ergebnis
        tolerance = 1e-6
        if (abs(x - x2_check) < tolerance and 
            abs(y - y2_check) < tolerance and 
            abs(z - z2_check) < tolerance):
            st.write("Die Schnittpunkte stimmen überein (innerhalb der Toleranz). Die Geraden schneiden sich im Punkt:")
            st.write(f"Schnittpunkt: [{x:.3f}, {y:.3f}, {z:.3f}]")
        else:
            st.write("Die Schnittpunkte stimmen nicht überein. Die Geraden sind windschief.")
