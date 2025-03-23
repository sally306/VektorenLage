import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Ausführliche Analyse")

# Beschreibung
st.write("""
Geben Sie die Stütz- und Richtungsvektoren für zwei Geraden im ℝ³ ein. 
Wir untersuchen ihre Lagebeziehung (parallel, schneidend, windschief, identisch) 
und berechnen bei sich schneidenden Geraden den Schnittpunkt.
Die Schritte folgen exakt der Methode aus dem Beispielbild.
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
    rz1 = st.number_input("rz1", value=2.0, step=1.0, key="rz1")

# Eingabefelder für die zweite Gerade
st.header("Gerade 2")
col3, col4 = st.columns(2)

with col3:
    st.subheader("Stützvektor g2")
    x2 = st.number_input("x2", value=0.0, step=1.0, key="x2")
    y2 = st.number_input("y2", value=1.0, step=1.0, key="y2")
    z2 = st.number_input("z2", value=0.0, step=1.0, key="z2")

with col4:
    st.subheader("Richtungsvektor r2")
    rx2 = st.number_input("rx2", value=1.0, step=1.0, key="rx2")
    ry2 = st.number_input("ry2", value=2.0, step=1.0, key="ry2")
    rz2 = st.number_input("rz2", value=1.0, step=1.0, key="rz2")

# Vektoren als Listen definieren
g1 = [x1, y1, z1]
r1 = [rx1, ry1, rz1]
g2 = [x2, y2, z2]
r2 = [rx2, ry2, rz2]

# Funktion für Vektorsubtraktion
def vector_subtract(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

# Funktion für Vektoraddition mit Skalar
def vector_add_scalar(v, scalar, direction):
    return [v[0] + scalar * direction[0], v[1] + scalar * direction[1], v[2] + scalar * direction[2]]

# Berechnungen durchführen
if st.button("Lagebeziehung berechnen"):
    st.header("Schritt-für-Schritt-Analyse auf Oberstufen-Niveau")

    # Schritt 1: Geradengleichungen
    st.subheader("Schritt 1: Geradengleichungen aufstellen")
    st.write("Die parametrische Form einer Geraden ist: **x = g + t * r**.")
    st.write("Für Gerade 1:")
    st.write(f"g1 = {g1}, r1 = {r1}")
    st.write(f"x = {g1[0]} + t * {r1[0]}")
    st.write(f"y = {g1[1]} + t * {r1[1]}")
    st.write(f"z = {g1[2]} + t * {r1[2]}")
    st.write("Für Gerade 2:")
    st.write(f"g2 = {g2}, r2 = {r2}")
    st.write(f"x = {g2[0]} + s * {r2[0]}")
    st.write(f"y = {g2[1]} + s * {r2[1]}")
    st.write(f"z = {g2[2]} + s * {r2[2]}")

    # Schritt 2: Prüfung auf Parallelität
    st.subheader("Schritt 2: Prüfung auf Parallelität")
    st.write("Zwei Geraden sind parallel, wenn ihre Richtungsvektoren Vielfache sind: r2 = λ * r1.")
    st.write(f"r1 = {r1}, r2 = {r2}")
    
    # Prüfung, ob r1 und r2 Vielfache sind
    parallel = True
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
            parallel = False
            break
    
    if parallel and lambda_values:
        first_lambda = lambda_values[0]
        for lam in lambda_values[1:]:
            if abs(lam - first_lambda) > 1e-10:
                parallel = False
                st.write(f"λ-Werte unterschiedlich: {lambda_values} → keine Vielfachen!")
                break
        if parallel:
            st.write(f"Die Richtungsvektoren sind Vielfache (λ = {first_lambda}), also sind die Geraden parallel.")
            
            # Schritt 2.1: Prüfung, ob Stützpunkt g2 auf Gerade 1 liegt
            st.subheader("Schritt 2.1: Prüfung, ob Stützpunkt g2 auf Gerade 1 liegt")
            st.write("Da die Geraden parallel sind, prüfen wir, ob sie identisch sind.")
            st.write("Dazu prüfen wir, ob der Stützvektor g2 auf Gerade 1 liegt.")
            st.write("Das bedeutet, es muss ein t existieren, sodass g2 = g1 + t * r1.")
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
                    if abs(t_val - first_t) > 1e-10:
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
        st.write("Die Richtungsvektoren sind keine Vielfachen, also sind die Geraden nicht parallel.")
        
        # Schritt 3: Schnittpunktprüfung mit Gauß-Verfahren
        st.subheader("Schritt 3: Gibt es einen Schnittpunkt? (Gauß-Verfahren)")
        st.write("Da die Geraden nicht parallel sind, prüfen wir, ob sie sich schneiden.")
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
        
        # Erweiterte Koeffizientenmatrix aufstellen
        matrix = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]
        
        st.write("Wir schreiben das System als erweiterte Koeffizientenmatrix:")
        matrix_display = f"    t     s     \n"
        matrix_display += f"  {matrix[0][0]:>5} {matrix[0][1]:>5} | {matrix[0][2]:>5}\n"
        matrix_display += f"  {matrix[1][0]:>5} {matrix[1][1]:>5} | {matrix[1][2]:>5}\n"
        matrix_display += f"  {matrix[2][0]:>5} {matrix[2][1]:>5} | {matrix[2][2]:>5}\n"
        st.code(matrix_display)
        
        # Gauß-Verfahren Schritt-für-Schritt
        st.write("(1) Ziel: Eliminieren von t in den Gleichungen II und III")
        # Finde das erste nicht-null Pivot in der ersten Spalte
        pivot_row = 0
        for i in range(3):
            if abs(matrix[i][0]) > 1e-10:
                pivot_row = i
                break
        else:
            st.write("Alle Koeffizienten von t sind 0. Wir prüfen die Gleichungen auf Konsistenz.")
            consistent = True
            s_values = []
            for i in range(3):
                if abs(matrix[i][1]) > 1e-10:
                    s_val = matrix[i][2] / matrix[i][1]
                    s_values.append(s_val)
                    st.write(f"Gleichung {i+1}: s = {matrix[i][2]} / {matrix[i][1]} = {s_val}")
                elif abs(matrix[i][2]) > 1e-10:
                    st.write(f"Gleichung {i+1}: 0 = {matrix[i][2]} → Widerspruch!")
                    consistent = False
                    break
            if consistent and s_values:
                s = s_values[0]
                for s_val in s_values[1:]:
                    if abs(s_val - s) > 1e-10:
                        consistent = False
                        break
                if consistent:
                    st.write(f"Alle Gleichungen sind konsistent, s = {s}. Da t nicht vorkommt, ist t frei.")
                    st.write("Die Geraden schneiden sich nicht (windschief oder parallel in einer Ebene).")
                else:
                    st.write("Die Gleichungen sind nicht konsistent. Die Geraden sind windschief.")
            else:
                st.write("Die Gleichungen sind nicht konsistent. Die Geraden sind windschief.")
            st.stop()
        
        # Vertausche Zeile 1 mit der Pivot-Zeile, falls nötig
        if pivot_row != 0:
            st.write(f"Vertausche Zeile 1 mit Zeile {pivot_row + 1}, um ein nicht-null Pivot zu erhalten:")
            matrix[0], matrix[pivot_row] = matrix[pivot_row], matrix[0]
            matrix_display = f"    t     s     \n"
            matrix_display += f"  {matrix[0][0]:>5.2f} {matrix[0][1]:>5.2f} | {matrix[0][2]:>5.2f}\n"
            matrix_display += f"  {matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} | {matrix[1][2]:>5.2f}\n"
            matrix_display += f"  {matrix[2][0]:>5.2f} {matrix[2][1]:>5.2f} | {matrix[2][2]:>5.2f}\n"
            st.code(matrix_display)
        
        pivot1 = matrix[0][0]
        # Eliminieren von t in Zeile 2 und 3
        for i in range(1, 3):
            if abs(matrix[i][0]) > 1e-10:
                factor = matrix[i][0] / pivot1
                st.write(f"Faktor für Zeile {i+1}: {matrix[i][0]} / {pivot1} = {factor}")
                for j in range(3):
                    matrix[i][j] -= factor * matrix[0][j]
            else:
                st.write(f"Zeile {i+1} hat bereits 0 in Spalte 1, keine Operation nötig.")
        
        st.write("Nach der Elimination:")
        matrix_display = f"    t     s     \n"
        matrix_display += f"  {matrix[0][0]:>5.2f} {matrix[0][1]:>5.2f} | {matrix[0][2]:>5.2f}\n"
        matrix_display += f"  {matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} | {matrix[1][2]:>5.2f}\n"
        matrix_display += f"  {matrix[2][0]:>5.2f} {matrix[2][1]:>5.2f} | {matrix[2][2]:>5.2f}\n"
        st.code(matrix_display)
        
        # (2) Koeffizient von s in Zeile 2 auf 1 bringen
        st.write("(2) Ziel: Koeffizient von s in Gleichung II auf 1 bringen")
        pivot_row = 1
        for i in range(1, 3):
            if abs(matrix[i][1]) > 1e-10:
                pivot_row = i
                break
        else:
            st.write("Alle Koeffizienten von s in Zeile 2 und 3 sind 0. Wir prüfen die Gleichungen auf Konsistenz.")
            consistent = True
            for i in range(1, 3):
                if abs(matrix[i][2]) > 1e-10:
                    st.write(f"Gleichung {i+1}: 0 = {matrix[i][2]} → Widerspruch!")
                    consistent = False
                    break
            if consistent:
                t = matrix[0][2] / matrix[0][0] if abs(matrix[0][0]) > 1e-10 else 0
                st.write(f"Alle Gleichungen sind konsistent, t = {t}. Da s nicht vorkommt, ist s frei.")
                st.write("Die Geraden schneiden sich nicht (windschief oder parallel in einer Ebene).")
            else:
                st.write("Die Gleichungen sind nicht konsistent. Die Geraden sind windschief.")
            st.stop()
        
        # Vertausche Zeile 2 mit der Pivot-Zeile, falls nötig
        if pivot_row != 1:
            st.write(f"Vertausche Zeile 2 mit Zeile {pivot_row + 1}, um ein nicht-null Pivot zu erhalten:")
            matrix[1], matrix[pivot_row] = matrix[pivot_row], matrix[1]
            matrix_display = f"    t     s     \n"
            matrix_display += f"  {matrix[0][0]:>5.2f} {matrix[0][1]:>5.2f} | {matrix[0][2]:>5.2f}\n"
            matrix_display += f"  {matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} | {matrix[1][2]:>5.2f}\n"
            matrix_display += f"  {matrix[2][0]:>5.2f} {matrix[2][1]:>5.2f} | {matrix[2][2]:>5.2f}\n"
            st.code(matrix_display)
        
        pivot2 = matrix[1][1]
        st.write(f"Dividiere Zeile 2 durch {pivot2}:")
        for j in range(3):
            matrix[1][j] /= pivot2
        
        matrix_display = f"    t     s     \n"
        matrix_display += f"  {matrix[0][0]:>5.2f} {matrix[0][1]:>5.2f} | {matrix[0][2]:>5.2f}\n"
        matrix_display += f"  {matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} | {matrix[1][2]:>5.2f}\n"
        matrix_display += f"  {matrix[2][0]:>5.2f} {matrix[2][1]:>5.2f} | {matrix[2][2]:>5.2f}\n"
        st.code(matrix_display)
        
        # (3) Eliminieren von s in Zeile 1 und 3
        st.write("(3) Ziel: Eliminieren von s in den Gleichungen I und III")
        for i in [0, 2]:
            if abs(matrix[i][1]) > 1e-10:
                factor = matrix[i][1] / matrix[1][1]
                st.write(f"Faktor für Zeile {i+1}: {matrix[i][1]} / {matrix[1][1]} = {factor}")
                for j in range(3):
                    matrix[i][j] -= factor * matrix[1][j]
            else:
                st.write(f"Zeile {i+1} hat bereits 0 in Spalte 2, keine Operation nötig.")
        
        st.write("Nach der Elimination:")
        matrix_display = f"    t     s     \n"
        matrix_display += f"  {matrix[0][0]:>5.2f} {matrix[0][1]:>5.2f} | {matrix[0][2]:>5.2f}\n"
        matrix_display += f"  {matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} | {matrix[1][2]:>5.2f}\n"
        matrix_display += f"  {matrix[2][0]:>5.2f} {matrix[2][1]:>5.2f} | {matrix[2][2]:>5.2f}\n"
        st.code(matrix_display)
        
        # (4) Analyse der Stufenform
        st.write("(4) Analyse der Stufenform")
        if abs(matrix[2][0]) < 1e-10 and abs(matrix[2][1]) < 1e-10:
            if abs(matrix[2][2]) < 1e-10:
                st.write("Die dritte Zeile ist 0 = 0, das System ist lösbar.")
                t = matrix[0][2] / matrix[0][0] if abs(matrix[0][0]) > 1e-10 else None
                s = matrix[1][2]
                st.write(f"t = {t}, s = {s}")
                
                if t is not None:
                    # Schrittweise Schnittpunktberechnung
                    st.subheader("Schritt 3.1: Schnittpunkt schrittweise berechnen")
                    st.write("Wir berechnen den Schnittpunkt mit t in Gerade 1:")
                    x = g1[0] + t * r1[0]
                    y = g1[1] + t * r1[1]
                    z = g1[2] + t * r1[2]
                    st.write(f"x = {g1[0]} + {t} * {r1[0]} = {x}")
                    st.write(f"y = {g1[1]} + {t} * {r1[1]} = {y}")
                    st.write(f"z = {g1[2]} + {t} * {r1[2]} = {z}")
                    schnittpunkt = [x, y, z]
                    st.write(f"Schnittpunkt: {schnittpunkt}")
                    
                    # Überprüfung mit Gerade 2
                    st.write("Überprüfung mit s in Gerade 2:")
                    x2_check = g2[0] + s * r2[0]
                    y2_check = g2[1] + s * r2[1]
                    z2_check = g2[2] + s * r2[2]
                    st.write(f"x = {g2[0]} + {s} * {r2[0]} = {x2_check}")
                    st.write(f"y = {g2[1]} + {s} * {r2[1]} = {y2_check}")
                    st.write(f"z = {g2[2]} + {s} * {r2[2]} = {z2_check}")
                    schnittpunkt2 = [x2_check, y2_check, z2_check]
                    st.write(f"Schnittpunkt (Gerade 2): {schnittpunkt2}")
                    
                    if (abs(x - x2_check) < 1e-10 and 
                        abs(y - y2_check) < 1e-10 and 
                        abs(z - z2_check) < 1e-10):
                        st.write("Die Schnittpunkte stimmen überein. Die Geraden schneiden sich Windschief im Punkt:")
                        st.write(f"Schnittpunkt: {schnittpunkt}")
                    else:
                        st.write("Die Schnittpunkte stimmen nicht überein. Das System ist nicht korrekt gelöst.")
                        st.write("Die Geraden sind windschief.")
                else:
                    st.write("Der Koeffizient von t in Zeile 1 ist 0, das System ist nicht eindeutig lösbar.")
                    st.write("Die Geraden sind windschief.")
            else:
                st.write(f"Die dritte Zeile ist 0 = {matrix[2][2]:.2f}, ein Widerspruch. Das System hat keine Lösung.")
                st.write("Die Geraden sind windschief.")
        else:
            st.write("Die dritte Zeile ist nicht in der Form 0 = c, das System ist nicht lösbar.")
            st.write("Die Geraden sind windschief.")
