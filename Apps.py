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
    ry1 = st.number_input("ry1", value=1.0, step=1.0, key="ry1")
    rz1 = st.number_input("rz1", value=1.0, step=1.0, key="rz1")

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
    ry2 = st.number_input("ry2", value=1.0, step=1.0, key="ry2")
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

# Funktion für 3D-Koordinatensystem (textbasiert, 2D-Projektion)
def draw_3d_coordinate_system(g1, r1, g2, r2, schnittpunkt=None):
    width, height = 20, 20  # Größe der 2D-Projektion
    grid = [['.' for _ in range(width)] for _ in range(height)]
    scale = 2  # Skalierung für die Darstellung
    
    # Koordinatenachsen zeichnen (perspektivische Projektion)
    center_x, center_y = width // 2, height // 2
    
    # x-Achse
    for x in range(width):
        grid[center_y][x] = '-'
    # y-Achse
    for y in range(height):
        grid[y][center_x] = '|'
    # z-Achse (perspektivisch: diagonal von unten links nach oben rechts)
    for i in range(min(width, height)):
        if 0 <= center_y - i < height and 0 <= center_x + i < width:
            grid[center_y - i][center_x + i] = '/'
    grid[center_y][center_x] = '+'  # Ursprung
    
    # Gerade 1: Stützvektor und Gerade (Projektion auf xy-Ebene mit z-Einfluss)
    g1_x = int(g1[0] / scale + center_x + g1[2] / scale)  # z-Einfluss für Perspektive
    g1_y = int(g1[1] / scale + center_y - g1[2] / scale)  # z-Einfluss für Perspektive
    if 0 <= g1_x < width and 0 <= g1_y < height:
        grid[g1_y][g1_x] = 'G'  # Stützvektor g1
    
    # Gerade 1 zeichnen
    for t in range(-5, 6):
        x = g1[0] + t * r1[0]
        y = g1[1] + t * r1[1]
        z = g1[2] + t * r1[2]
        proj_x = int(x / scale + center_x + z / scale)  # Perspektivische Projektion
        proj_y = int(y / scale + center_y - z / scale)
        if 0 <= proj_x < width and 0 <= proj_y < height and grid[proj_y][proj_x] not in ['+', 'G']:
            grid[proj_y][proj_x] = '1'
    
    # Gerade 2: Stützvektor und Gerade
    g2_x = int(g2[0] / scale + center_x + g2[2] / scale)
    g2_y = int(g2[1] / scale + center_y - g2[2] / scale)
    if 0 <= g2_x < width and 0 <= g2_y < height:
        grid[g2_y][g2_x] = 'H'  # Stützvektor g2
    
    # Gerade 2 zeichnen
    for s in range(-5, 6):
        x = g2[0] + s * r2[0]
        y = g2[1] + s * r2[1]
        z = g2[2] + s * r2[2]
        proj_x = int(x / scale + center_x + z / scale)
        proj_y = int(y / scale + center_y - z / scale)
        if 0 <= proj_x < width and 0 <= proj_y < height and grid[proj_y][proj_x] not in ['+', 'H']:
            grid[proj_y][proj_x] = '2'
    
    # Schnittpunkt markieren
    if schnittpunkt:
        x, y, z = schnittpunkt
        proj_x = int(x / scale + center_x + z / scale)
        proj_y = int(y / scale + center_y - z / scale)
        if 0 <= proj_x < width and 0 <= proj_y < height:
            grid[proj_y][proj_x] = 'X'
    
    # Grid als String formatieren (mit Achsenbeschriftungen)
    drawing = "  y\n"
    for y in range(height):
        row = "".join(grid[y])
        drawing += f"{height // 2 - y:2d} {row}\n"
    drawing += "   " + "".join([f"{i - center_x:2d}" for i in range(width)]) + " x\n"
    return drawing

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
            
            # Prüfung, ob Stützpunkt g2 auf Gerade 1 liegt
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
            
            st.subheader("3D-Koordinatensystem (perspektivische Projektion)")
            st.write("Legende: G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2")
            drawing = draw_3d_coordinate_system(g1, r1, g2, r2)
            st.code(drawing)
    else:
        st.write("Die Richtungsvektoren sind keine Vielfachen, also sind die Geraden nicht parallel.")
        
        # Schritt 3: Schnittpunktprüfung (vollständig auch für windschief)
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
        
        # Lösen der ersten zwei Gleichungen (verbessert für alle Fälle)
        st.write("Wir lösen die ersten zwei Gleichungen nach t und s:")
        a1, b1, c1 = r1[0], -r2[0], g2[0] - g1[0]
        a2, b2, c2 = r1[1], -r2[1], g2[1] - g1[1]
        
        st.write(f"I.   {a1} * t + ({b1}) * s = {c1}")
        st.write(f"II.  {a2} * t + ({b2}) * s = {c2}")
        
        # Schrittweise Lösung
        t = None
        s = None
        
        # Determinante berechnen, um zu prüfen, ob das Gleichungssystem lösbar ist
        det = a1 * b2 - a2 * b1
        if det != 0:
            # Nach t und s auflösen (Cramer'sche Regel)
            t = (c1 * b2 - c2 * b1) / det
            s = (a1 * c2 - a2 * c1) / det
            st.write(f"Determinante: {det}")
            st.write(f"t = ({c1} * {b2} - {c2} * {b1}) / {det} = {t}")
            st.write(f"s = ({a1} * {c2} - {a2} * {c1}) / {det} = {s}")
        else:
            st.write("Determinante ist 0, keine eindeutige Lösung möglich.")
        
        # Konsistenzprüfung
        st.subheader("Schritt 3.1: Konsistenzprüfung mit Gleichung III")
        if t is not None and s is not None:
            st.write("Setze t und s in die dritte Gleichung ein:")
            left = g1[2] + t * r1[2]
            right = g2[2] + s * r2[2]
            st.write(f"III. {g1[2]} + t * {r1[2]} = {g2[2]} + s * {r2[2]}")
            st.write(f"     {g1[2]} + {t} * {r1[2]} = {g2[2]} + {s} * {r2[2]}")
            st.write(f"     {left} = {right}")
            
            if abs(left - right) < 1e-10:
                st.write("Die dritte Gleichung ist erfüllt → Die Geraden schneiden sich!")
                schnittpunkt = vector_add_scalar(g1, t, r1)
                st.write("Berechne den Schnittpunkt mit t in Gerade 1:")
                st.write(f"x = {g1[0]} + {t} * {r1[0]} = {schnittpunkt[0]}")
                st.write(f"y = {g1[1]} + {t} * {r1[1]} = {schnittpunkt[1]}")
                st.write(f"z = {g1[2]} + {t} * {r1[2]} = {schnittpunkt[2]}")
                st.write(f"Schnittpunkt: {schnittpunkt}")
                st.subheader("3D-Koordinatensystem (perspektivische Projektion)")
                st.write("Legende: G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2, X = Schnittpunkt")
                drawing = draw_3d_coordinate_system(g1, r1, g2, r2, schnittpunkt)
                st.code(drawing)
            else:
                st.write("Die dritte Gleichung ist nicht erfüllt → Die Geraden sind windschief.")
                st.write(f"Ergebnis: Keine konsistente Lösung, die Geraden sind windschief.")
                st.subheader("3D-Koordinatensystem (perspektivische Projektion)")
                st.write("Legende: G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2")
                drawing = draw_3d_coordinate_system(g1, r1, g2, r2)
                st.code(drawing)
        else:
            st.write("Keine Lösung für t und s gefunden → Die Geraden sind windschief.")
            st.subheader("3D-Koordinatensystem (perspektivische Projektion)")
            st.write("Legende: G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2")
            drawing = draw_3d_coordinate_system(g1, r1, g2, r2)
            st.code(drawing)
