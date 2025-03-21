import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Mit Visualisierung")

# Beschreibung
st.write("""
Geben Sie die Stütz- und Richtungsvektoren für zwei Geraden im ℝ³ ein. 
Wir untersuchen ihre Lagebeziehung (parallel, schneidend, windschief) 
und berechnen bei sich schneidenden Geraden den Schnittpunkt.
Zusätzlich wird eine einfache 2D-Visualisierung (xy-Projektion) erstellt.
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

# Funktion für Kreuzprodukt
def cross_product(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Funktion für Vektorsubtraktion
def vector_subtract(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

# Funktion für Vektoraddition mit Skalar
def vector_add_scalar(v, scalar, direction):
    return [v[0] + scalar * direction[0], v[1] + scalar * direction[1], v[2] + scalar * direction[2]]

# Funktion für einfache 2D-Visualisierung (xy-Projektion)
def draw_lines_2d(g1, r1, g2, r2, schnittpunkt=None):
    # Größe des "Bildes"
    width, height = 20, 10
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Skalierungsfaktor
    scale = 2  # Passt die Darstellung an kleine Werte an
    
    # Gerade 1 zeichnen (xy-Projektion)
    for t in range(-5, 6):
        x = int(g1[0] + t * r1[0]) // scale + width // 2
        y = int(g1[1] + t * r1[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '-'
    
    # Gerade 2 zeichnen (xy-Projektion)
    for s in range(-5, 6):
        x = int(g2[0] + s * r2[0]) // scale + width // 2
        y = int(g2[1] + s * r2[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '|'
    
    # Schnittpunkt markieren, falls vorhanden
    if schnittpunkt:
        x = int(schnittpunkt[0]) // scale + width // 2
        y = int(schnittpunkt[1]) // scale + height // 2
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = 'X'
    
    # Grid als String formatieren
    drawing = "\n".join("".join(row) for row in grid)
    return drawing

# Berechnungen durchführen
if st.button("Lagebeziehung berechnen"):
    st.header("Schritt-für-Schritt-Analyse auf Oberstufen-Niveau")
    
    # Schritt 1: Geradengleichungen aufstellen
    st.subheader("Schritt 1: Geradengleichungen aufstellen")
    st.write("Im Raum ℝ³ wird eine Gerade durch einen Stützvektor und einen Richtungsvektor definiert.")
    st.write("Die parametrische Form lautet: **x = g + t * r**, wobei t ein Parameter ist.")
    st.write("Für Gerade 1:")
    st.write(f"g1 = {g1}, r1 = {r1}")
    st.write("Komponentenweise:")
    st.write(f"x = {g1[0]} + t * {r1[0]}")
    st.write(f"y = {g1[1]} + t * {r1[1]}")
    st.write(f"z = {g1[2]} + t * {r1[2]}")
    st.write("Für Gerade 2:")
    st.write(f"g2 = {g2}, r2 = {r2}")
    st.write("Komponentenweise:")
    st.write(f"x = {g2[0]} + s * {r2[0]}")
    st.write(f"y = {g2[1]} + s * {r2[1]}")
    st.write(f"z = {g2[2]} + s * {r2[2]}")

    # Schritt 2: Parallelitätsprüfung
    st.subheader("Schritt 2: Prüfung auf Parallelität")
    st.write("Zwei Geraden sind parallel, wenn ihre Richtungsvektoren Vielfache voneinander sind.")
    st.write("Das heißt, es muss ein λ existieren, sodass r2 = λ * r1 gilt.")
    st.write(f"Gegeben: r1 = {r1}, r2 = {r2}")
    st.write("Wir prüfen die Komponenten:")

    parallel = True
    lambda_values = []
    for i in range(3):
        if r1[i] != 0:
            lambda_val = r2[i] / r1[i]
            lambda_values.append(lambda_val)
            st.write(f"Komponente {i+1}: {r2[i]} / {r1[i]} = {lambda_val}")
        elif r2[i] == 0:
            st.write(f"Komponente {i+1}: Beide sind 0, passt.")
        else:
            st.write(f"Komponente {i+1}: r1[{i}] = 0, aber r2[{i}] = {r2[i]} ≠ 0 → kein Vielfaches!")
            parallel = False
            break
    
    if parallel and lambda_values:
        first_lambda = lambda_values
