import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Ausführliche Analyse")

# Beschreibung
st.write("""
Geben Sie die Stütz- und Richtungsvektoren für zwei Geraden im ℝ³ ein. 
Wir untersuchen ihre Lagebeziehung (parallel, schneidend, windschief) 
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
    ry1 = st.number_input("ry1", value=0.0, step=1.0, key="ry1")
    rz1 = st.number_input("rz1", value=0.0, step=1.0, key="rz1")

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
    rx2 = st.number_input("rx2", value=0.0, step=1.0, key="rx2")
    ry2 = st.number_input("ry2", value=1.0, step=1.0, key="ry2")
    rz2 = st.number_input("rz2", value=0.0, step=1.0, key="rz2")

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

# Funktion für 2D-Visualisierung (xy-Projektion)
def draw_lines_2d(g1, r1, g2, r2, schnittpunkt=None):
    width, height = 20, 10
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    scale = 2
    
    for t in range(-5, 6):
        x = int(g1[0] + t * r1[0]) // scale + width // 2
        y = int(g1[1] + t * r1[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '-'
    
    for s in range(-5, 6):
        x = int(g2[0] + s * r2[0]) // scale + width // 2
        y = int(g2[1] + s * r2[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '|'
    
    if schnittpunkt:
        x = int(schnittpunkt[0]) // scale + width // 2
        y = int(schnittpunkt[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = 'X'
    
    return "\n".join("".join(row) for row in grid)

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

    # Schritt 2: Parallelitätsprüfung
    st.subheader("Schritt 2: Prüfung auf Parallelität")
    st.write("Zwei Geraden sind parallel, wenn ihre Richtungsvektoren Vielfache sind: r2 = λ * r1.")
    st.write(f"r1 = {r1}, r2 = {r2}")
    parallel = True
    lambda_values = []
    for i in range(3):
        if r1[i] != 0:
            lambda_val = r2[i] / r1[i]
            lambda_values.append(lambda_val)
            st.write(f"Komponente {i+1}: {r2[i]} / {r1[i]} = {lambda_val}")
        elif r2[i] == 0:
            st.write(f"Komponente {i+1}: Beide 0, passt.")
        else:
            st.write(f"Komponente {i+1}: r1[{i}] = 0, r2[{i}] = {r2[i]} ≠ 0 → kein Vielfaches!")
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
            st.write("Da die Geraden parallel sind, können sie keinen Schnittpunkt haben.")
            st.write("Wir prüfen nicht weiter, da parallele Geraden entweder identisch oder echt parallel sind.")
            st.subheader("Visualisierung (xy-Projektion)")
            drawing = draw_lines_2d(g1, r1, g2, r2)
            st.code(drawing)
    else:
        st.write("Die Richtungsvektoren sind keine Vielfachen, also sind die Geraden nicht parallel.")
        
        # Schritt 3: Schnittpunktprüfung
        st.subheader("Schritt 3: Gibt es einen Schnittpunkt?")
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
        
        # Lösen der ersten zwei Gleichungen
        st.write("Wir lösen die ersten zwei Gleichungen nach t und s:")
        a1, b1, c1 = r1[0], -r2[0], g2[0] - g1[0]
        a2, b2, c2 = r1[1], -r2[1], g2[1] - g1[1]
        
        st.write(f"I.   {a1} * t + ({b1}) * s = {c1}")
        st.write(f"II.  {a2} * t + ({b2}) * s = {c2}")
        
        # Schrittweise Lösung wie im Bild
        st.write("Nach t auflösen in Gleichung I:")
        if a1 != 0:
            t_expr = f"t = ({c1} - ({b1}) * s) / {a1}"
            st.write(f"I.   {t_expr}")
        else:
            st.write("Koeffizient von t in I ist 0, wir lösen direkt nach s:")
            s = c1 / b1 if b1 != 0 else None
            st.write(f"s = {c1} / ({b1}) = {s}")
            t = None
        
        if t is None and s is not None:
            st.write("Setze s in II ein:")
            t = (c2 - b2 * s) / a2 if a2 != 0 else None
            st.write(f"II.  {a2} * t + ({b2}) * {s} = {c2}")
            st.write(f"     {a2} * t = {c2} - ({b2}) * {s}")
            st.write(f"     t = ({c2} - ({b2}) * {s}) / {a2} = {t}")
        else:
            st.write("Setze t in II ein:")
            st.write(f"II.  {a2} * ({c1} - ({b1}) * s) / {a1} + ({b2}) * s = {c2}")
            st.write(f"     {a2} * ({c1} - ({b1}) * s) / {a1} + ({b2}) * s = {c2}")
            st.write(f"     {a2} * ({c1} - ({b1}) * s) + ({b2}) * s * {a1} = {c2} * {a1}")
            st.write(f"     {a2} * {c1} - {a2} * ({b1}) * s + ({b2}) * s * {a1} = {c2} * {a1}")
            st.write(f"     {a2} * {c1} + s * (-{a2} * ({b1}) + ({b2}) * {a1}) = {c2} * {a1}")
            coeff_s = -a2 * b1 + b2 * a1
            const = c2 * a1 - a2 * c1
            st.write(f"     s * ({coeff_s}) = {const}")
            if coeff_s != 0:
                s = const / coeff_s
                st.write(f"     s = {const} / ({coeff_s}) = {s}")
            else:
                st.write("Koeffizient von s ist 0, keine Lösung möglich.")
                s = None
            
            if s is not None:
                st.write("Setze s in I ein, um t zu berechnen:")
                t = (c1 - b1 * s) / a1 if a1 != 0 else None
                st.write(f"t = ({c1} - ({b1}) * {s}) / {a1} = {t}")
        
        # Konsistenzprüfung
        if t is not None and s is not None:
            st.subheader("Schritt 3.1: Konsistenzprüfung mit Gleichung III")
            st.write("Setze t und s in die dritte Gleichung ein:")
            left = g1[2] + t * r1[2]
            right = g2[2] + s * r2[2]
            st.write(f"III. {g1[2]} + t * {r1[2]} = {g2[2]} + s * {r2[2]}")
            st.write(f"     {g1[2]} + {t} * {r1[2]} = {g2[2]} + {s} * {r2[2]}")
            st.write(f"     {left} = {right}")
            
            if abs(left - right) < 1e-10:
                st.write("Die dritte Gleichung ist erfüllt → Schnittpunkt existiert!")
                schnittpunkt = vector_add_scalar(g1, t, r1)
                st.write("Berechne den Schnittpunkt mit t in Gerade 1:")
                st.write(f"x = {g1[0]} + {t} * {r1[0]} = {schnittpunkt[0]}")
                st.write(f"y = {g1[1]} + {t} * {r1[1]} = {schnittpunkt[1]}")
                st.write(f"z = {g1[2]} + {t} * {r1[2]} = {schnittpunkt[2]}")
                st.write(f"Schnittpunkt: {schnittpunkt}")
                st.subheader("Visualisierung (xy-Projektion)")
                drawing = draw_lines_2d(g1, r1, g2, r2, schnittpunkt)
                st.code(drawing)
            else:
                st.write("Die dritte Gleichung ist nicht erfüllt → Die Geraden sind windschief.")
                st.write(f"Ergebnis: Keine Lösung, die Geraden sind windschief.")
                st.subheader("Visualisierung (xy-Projektion)")
                drawing = draw_lines_2d(g1, r1, g2, r2)
                st.code(drawing)
        else:
            st.write("Keine Lösung für t und s gefunden → Die Geraden sind windschief.")
            st.subheader("Visualisierung (xy-Projektion)")
            drawing = draw_lines_2d(g1, r1, g2, r2)
            st.code(drawing)
