import streamlit as st

# Titel der Anwendung
st.title("Lagebeziehungen von Geraden im Raum - Ausführliche Analyse")

# Beschreibung
st.write("""
Geben Sie die Stütz- und Richtungsvektoren für zwei Geraden im ℝ³ ein. 
Wir untersuchen ihre Lagebeziehung (parallel, schneidend, windschief) 
und berechnen bei sich schneidenden Geraden den Schnittpunkt mit dem Gauß-Verfahren.
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

# Berechnungen durchführen
if st.button("Lagebeziehung berechnen"):
    st.header("Schritt-für-Schritt-Analyse")
    
    # Schritt 1: Geradengleichungen aufstellen
    st.subheader("Schritt 1: Geradengleichungen aufstellen")
    st.write("Eine Gerade im Raum wird parametrisch angegeben als: **x = Stützvektor + t * Richtungsvektor**.")
    st.write(f"Für Gerade 1: g1 = {g1}, r1 = {r1}")
    st.write(f"x = {g1[0]} + t * {r1[0]}")
    st.write(f"y = {g1[1]} + t * {r1[1]}")
    st.write(f"z = {g1[2]} + t * {r1[2]}")
    st.write(f"Für Gerade 2: g2 = {g2}, r2 = {r2}")
    st.write(f"x = {g2[0]} + s * {r2[0]}")
    st.write(f"y = {g2[1]} + s * {r2[1]}")
    st.write(f"z = {g2[2]} + s * {r2[2]}")

    # Schritt 2: Parallelitätsprüfung
    st.subheader("Schritt 2: Sind die Geraden parallel?")
    st.write("Zwei Geraden sind parallel, wenn ihre Richtungsvektoren ein Vielfaches voneinander sind.")
    st.write("Das überprüfen wir mit dem Kreuzprodukt: Wenn r1 × r2 = [0, 0, 0], sind sie parallel.")
    cross = cross_product(r1, r2)
    st.write(f"r1 = {r1}, r2 = {r2}")
    st.write("Kreuzprodukt berechnen:")
    st.write(f"x-Komponente: {r1[1]} * {r2[2]} - {r1[2]} * {r2[1]} = {cross[0]}")
    st.write(f"y-Komponente: {r1[2]} * {r2[0]} - {r1[0]} * {r2[2]} = {cross[1]}")
    st.write(f"z-Komponente: {r1[0]} * {r2[1]} - {r1[1]} * {r2[0]} = {cross[2]}")
    st.write(f"r1 × r2 = {cross}")

    if cross == [0, 0, 0]:
        st.write("Das Kreuzprodukt ist [0, 0, 0], also sind die Richtungsvektoren parallel.")
        st.subheader("Schritt 2.1: Identisch oder echt parallel?")
        st.write("Wir prüfen, ob der Verbindungsvektor g2 - g1 ein Vielfaches von r1 ist.")
        diff = vector_subtract(g2, g1)
        st.write(f"g2 - g1 = {g2} - {g1} = {diff}")
        diff_cross_r1 = cross_product(diff, r1)
        st.write(f"(g2 - g1) × r1 = {diff} × {r1} = {diff_cross_r1}")
        if diff_cross_r1 == [0, 0, 0]:
            st.write("Das Kreuzprodukt ist [0, 0, 0], die Geraden sind identisch.")
        else:
            st.write("Die Geraden sind echt parallel (kein Schnittpunkt).")
    else:
        st.write("Das Kreuzprodukt ist nicht [0, 0, 0], die Geraden sind nicht parallel.")
        
        # Schritt 3: Schnittpunktberechnung mit Gauß-Verfahren
        st.subheader("Schritt 3: Schnittpunkt berechnen")
        st.write("Wir setzen die Geradengleichungen gleich, um t und s zu finden:")
        st.write(f"1. {g1[0]} + t * {r1[0]} = {g2[0]} + s * {r2[0]}")
        st.write(f"2. {g1[1]} + t * {r1[1]} = {g2[1]} + s * {r2[1]}")
        st.write(f"3. {g1[2]} + t * {r1[2]} = {g2[2]} + s * {r2[2]}")
        
        st.write("Umstellen nach t und s:")
        eq1 = f"{r1[0]} * t - {r2[0]} * s = {g2[0]} - {g1[0]}"
        eq2 = f"{r1[1]} * t - {r2[1]} * s = {g2[1]} - {g1[1]}"
        eq3 = f"{r1[2]} * t - {r2[2]} * s = {g2[2]} - {g1[2]}"
        st.write(f"1. {eq1}")
        st.write(f"2. {eq2}")
        st.write(f"3. {eq3}")

        # Gauß-Verfahren
        st.subheader("Schritt 3.1: Gauß-Verfahren anwenden")
        st.write("Wir haben 3 Gleichungen, aber nur 2 Unbekannte (t und s).")
        st.write("Wir nehmen die ersten zwei Gleichungen und lösen sie:")
        st.write(f"1. {r1[0]} * t - {r2[0]} * s = {g2[0] - g1[0]}")
        st.write(f"2. {r1[1]} * t - {r2[1]} * s = {g2[1] - g1[1]}")
        
        # Koeffizientenmatrix und rechte Seite
        a11, a12 = r1[0], -r2[0]
        a21, a22 = r1[1], -r2[1]
        b1, b2 = g2[0] - g1[0], g2[1] - g1[1]
        
        st.write("Matrixform:")
        st.write(f"[ {a11}  {a12} | {b1} ]")
        st.write(f"[ {a21}  {a22} | {b2} ]")
        
        # Elimination
        if a11 == 0 and a21 == 0:
            st.write("Keine Lösung möglich (beide Koeffizienten für t sind 0).")
        else:
            if a11 != 0:
                factor = a21 / a11
                st.write(f"Elimination: Zeile 2 - ({factor}) * Zeile 1")
                new_a22 = a22 - factor * a12
                new_b2 = b2 - factor * b1
                st.write(f"Neue Zeile 2: 0 * t + {new_a22} * s = {new_b2}")
                
                if new_a22 != 0:
                    s = new_b2 / new_a22
                    st.write(f"s = {new_b2} / {new_a22} = {s}")
                    t = (b1 + r2[0] * s) / r1[0] if r1[0] != 0 else "undefiniert"
                    st.write(f"t = ({b1} + {r2[0]} * {s}) / {r1[0]} = {t}")
                else:
                    st.write("Keine eindeutige Lösung (windschief).")
                    t, s = None, None
            else:
                st.write("Vertausche Zeilen (falls nötig) und löse direkt.")
                s = b1 / a12 if a12 != 0 else "undefiniert"
                t = (b2 + r2[1] * s) / r1[1] if r1[1] != 0 else "undefiniert"
            
            if t is not None and s is not None:
                # Konsistenzprüfung mit der dritten Gleichung
                st.write("Schritt 3.2: Konsistenzprüfung mit 3. Gleichung")
                left = g1[2] + t * r1[2]
                right = g2[2] + s * r2[2]
                st.write(f"{g1[2]} + {t} * {r1[2]} = {left}")
                st.write(f"{g2[2]} + {s} * {r2[2]} = {right}")
                if abs(left - right) < 1e-10:
                    st.write("Die Geraden schneiden sich!")
                    schnittpunkt = vector_add_scalar(g1, t, r1)
                    st.write(f"Schnittpunkt: {g1} + {t} * {r1} = {schnittpunkt}")
                else:
                    st.write("Die Geraden sind windschief (dritte Gleichung nicht erfüllt).")
