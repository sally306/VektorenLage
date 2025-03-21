import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Analyse")

# Beschreibung
st.write("""
Wir analysieren die Lagebeziehung der folgenden Geraden, die aus dem Bild entnommen wurden:
- Gerade 1: x = [-1, 3, 35] + t * [3, 1, 1]
- Gerade 2: x = [-1, 30, 1] + s * [3, 1, 1]
""")

# Vektoren direkt einsetzen
g1 = [-1, 3, 35]
r1 = [3, 1, 1]
g2 = [-1, 30, 1]
r2 = [3, 1, 1]

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
        st.write(f"Alle λ gleich ({first_lambda}), die Geraden sind parallel!")

if parallel:
    st.write("Ergebnis: Die Geraden sind parallel.")
    st.subheader("Schritt 2.1: Identisch oder echt parallel?")
    st.write("Die Richtungsvektoren sind Vielfache, also sind die Geraden parallel.")
    st.write("Prüfen wir, ob sie identisch sind, indem wir den Verbindungsvektor g2 - g1 berechnen.")
    diff = vector_subtract(g2, g1)
    st.write(f"g2 - g1 = {g2} - {g1}")
    st.write(f"        = [{g2[0]} - ({g1[0]}), {g2[1]} - ({g1[1]}), {g2[2]} - ({g1[2]})]")
    st.write(f"        = [{g2[0] - g1[0]}, {g2[1] - g1[1]}, {g2[2] - g1[2]}]")
    st.write(f"        = {diff}")
    
    st.write("Nun prüfen wir, ob g2 - g1 ein Vielfaches von r1 ist, mit dem Kreuzprodukt (g2 - g1) × r1:")
    diff_cross_r1 = cross_product(diff, r1)
    st.write(f"x-Komponente: ({diff[1]} * {r1[2]}) - ({diff[2]} * {r1[1]}) = {diff_cross_r1[0]}")
    st.write(f"y-Komponente: ({diff[2]} * {r1[0]}) - ({diff[0]} * {r1[2]}) = {diff_cross_r1[1]}")
    st.write(f"z-Komponente: ({diff[0]} * {r1[1]}) - ({diff[1]} * {r1[0]}) = {diff_cross_r1[2]}")
    st.write(f"(g2 - g1) × r1 = {diff_cross_r1}")
    
    if diff_cross_r1 == [0, 0, 0]:
        st.write("Kreuzprodukt = [0, 0, 0] → Die Geraden sind identisch.")
    else:
        st.write("Kreuzprodukt ≠ [0, 0, 0] → Die Geraden sind echt parallel.")
    
    st.subheader("Visualisierung (xy-Projektion)")
    drawing = draw_lines_2d(g1, r1, g2, r2)
    st.code(drawing)
else:
    st.write("Ergebnis: Die Geraden sind nicht parallel.")
    
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
    
    a1, b1, c1 = r1[0], -r2[0], g2[0] - g1[0]
    a2, b2, c2 = r1[1], -r2[1], g2[1] - g1[1]
    det = a1 * b2 - a2 * b1
    st.write(f"Determinante der Koeffizienten (I und II):")
    st.write(f"det = ({a1} * {b2}) - ({a2} * {b1}) = {det}")
    
    if det == 0:
        st.write("Determinante = 0 → Die Gleichungen sind linear abhängig.")
        st.write("Da die Geraden nicht parallel sind, sind sie windschief.")
        st.subheader("Visualisierung (xy-Projektion)")
        drawing = draw_lines_2d(g1, r1, g2, r2)
        st.code(drawing)
    else:
        t = (c1 * b2 - c2 * b1) / det
        s = (a1 * c2 - a2 * c1) / det
        st.write(f"t = ({c1} * {b2} - {c2} * {b1}) / {det} = {t}")
        st.write(f"s = ({a1} * {c2} - {a2} * {c1}) / {det} = {s}")
        
        # Konsistenzprüfung
        st.subheader("Schritt 3.1: Konsistenzprüfung mit Gleichung III")
        left = g1[2] + t * r1[2]
        right = g2[2] + s * r2[2]
        st.write(f"Links:  {g1[2]} + {t} * {r1[2]} = {left}")
        st.write(f"Rechts: {g2[2]} + {s} * {r2[2]} = {right}")
        
        if abs(left - right) < 1e-10:
            st.write("Die dritte Gleichung ist erfüllt → Schnittpunkt existiert!")
            schnittpunkt = vector_add_scalar(g1, t, r1)
            st.write(f"Schnittpunkt: {g1} + {t} * {r1} = {schnittpunkt}")
            st.subheader("Visualisierung (xy-Projektion)")
            drawing = draw_lines_2d(g1, r1, g2, r2, schnittpunkt)
            st.code(drawing)
        else:
            st.write("Die dritte Gleichung ist nicht erfüllt → Die Geraden sind windschief.")
            st.subheader("Visualisierung (xy-Projektion)")
            drawing = draw_lines_2d(g1, r1, g2, r2)
            st.code(drawing)
