import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum")

# Beschreibung
st.write("""
Geben Sie die Stützvektoren und Richtungsvektoren für zwei Geraden ein, 
um ihre Lagebeziehung (parallel, schneidend, windschief) zu bestimmen.
Bei sich schneidenden Geraden wird der Schnittpunkt berechnet.
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
    y2 = st.number_input("y2", value=0.0, step=1.0, key="y2")
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

# Funktion für Kreuzprodukt ohne NumPy
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

# Berechnungen durchführen, wenn Button gedrückt wird
if st.button("Lagebeziehung berechnen"):
    st.header("Rechenweg und Ergebnisse")
    
    # Geradengleichungen anzeigen
    st.subheader("1. Geradengleichungen")
    st.write(f"g1: {g1} + t * {r1}")
    st.write(f"g2: {g2} + s * {r2}")

    # Prüfen, ob Richtungsvektoren parallel sind
    st.subheader("2. Prüfung auf Parallelität")
    cross = cross_product(r1, r2)
    st.write(f"Kreuzprodukt r1 × r2 = {r1} × {r2} = {cross}")
    
    if cross == [0, 0, 0]:
        st.write("Die Richtungsvektoren sind parallel (Kreuzprodukt = [0, 0, 0]).")
        
        # Prüfen, ob identisch oder echt parallel
        diff = vector_subtract(g2, g1)
        st.write(f"g2 - g1 = {g2} - {g1} = {diff}")
        diff_cross_r1 = cross_product(diff, r1)
        st.write(f"(g2 - g1) × r1 = {diff} × {r1} = {diff_cross_r1}")
        
        if diff_cross_r1 == [0, 0, 0]:
            st.write("Die Geraden sind identisch, da der Verbindungsvektor ein Vielfaches des Richtungsvektors ist.")
        else:
            st.write("Die Geraden sind echt parallel (kein gemeinsamer Punkt).")
    else:
        st.write("Die Richtungsvektoren sind nicht parallel.")
        
        # Schnittpunktberechnung
        st.subheader("3. Schnittpunktberechnung")
        st.write("Gleichungssystem: g1 + t * r1 = g2 + s * r2")
        st.write(f"1. {g1[0]} + t * {r1[0]} = {g2[0]} + s * {r2[0]}")
        st.write(f"2. {g1[1]} + t * {r1[1]} = {g2[1]} + s * {r2[1]}")
        st.write(f"3. {g1[2]} + t * {r1[2]} = {g2[2]} + s * {r2[2]}")
        
        # Lösen des Systems mit den ersten zwei Gleichungen
        # eq1: x1 + t * rx1 = x2 + s * rx2
        # eq2: y1 + t * ry1 = y2 + s * ry2
        try:
            # Koeffizienten für t und s
            a1, b1, c1 = r1[0], -r2[0], g2[0] - g1[0]
            a2, b2, c2 = r1[1], -r2[1], g2[1] - g1[1]
            
            # Determinante
            det = a1 * b2 - a2 * b1
            if det == 0:
                st.write("Die Geraden sind windschief oder parallel (Determinante = 0).")
            else:
                # Cramer'sche Regel
                t = (c1 * b2 - c2 * b1) / det
                s = (a1 * c2 - a2 * c1) / det
                
                st.write(f"t = {t}")
                st.write(f"s = {s}")
                
                # Prüfen der dritten Gleichung
                z_check = g1[2] + t * r1[2] - (g2[2] + s * r2[2])
                st.write(f"Überprüfung: {g1[2]} + {t} * {r1[2]} = {g2[2]} + {s} * {r2[2]}")
                st.write(f"Differenz in z-Richtung: {z_check}")
                
                if abs(z_check) < 1e-10:  # Numerische Genauigkeit
                    st.write("Die Geraden schneiden sich.")
                    schnittpunkt = vector_add_scalar(g1, t, r1)
                    st.write(f"Schnittpunkt = {g1} + {t} * {r1} = {schnittpunkt}")
                else:
                    st.write("Die Geraden sind windschief (kein Schnittpunkt, nicht parallel).")
        except ZeroDivisionError:
            st.write("Die Geraden sind windschief oder das Gleichungssystem ist nicht lösbar.")
