import streamlit as st
import numpy as np
from sympy import symbols, Eq, solve, latex

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

# Vektoren definieren
g1 = np.array([x1, y1, z1])
r1 = np.array([rx1, ry1, rz1])
g2 = np.array([x2, y2, z2])
r2 = np.array([rx2, ry2, rz2])

# Berechnungen durchführen, wenn Button gedrückt wird
if st.button("Lagebeziehung berechnen"):
    st.header("Rechenweg und Ergebnisse")
    
    # Geradengleichungen anzeigen
    st.subheader("1. Geradengleichungen")
    t, s = symbols('t s')
    g1_eq = f"g1: {latex(g1)} + t * {latex(r1)}"
    g2_eq = f"g2: {latex(g2)} + s * {latex(r2)}"
    st.latex(f"g_1: \\vec{{x}} = {g1_eq}")
    st.latex(f"g_2: \\vec{{x}} = {g2_eq}")

    # Prüfen, ob Richtungsvektoren parallel sind
    st.subheader("2. Prüfung auf Parallelität")
    cross_product = np.cross(r1, r2)
    st.latex(f"\\vec{{r_1}} \\times \\vec{{r_2}} = {latex(r1)} \\times {latex(r2)} = {latex(cross_product)}")
    
    if np.all(cross_product == 0):
        st.write("Die Richtungsvektoren sind parallel (Kreuzprodukt = 0).")
        
        # Prüfen, ob identisch oder echt parallel
        diff = g2 - g1
        st.latex(f"\\vec{{g_2}} - \\vec{{g_1}} = {latex(g2)} - {latex(g1)} = {latex(diff)}")
        
        if np.all(np.cross(diff, r1) == 0):
            st.write("Die Geraden sind identisch, da der Verbindungsvektor ein Vielfaches des Richtungsvektors ist.")
        else:
            st.write("Die Geraden sind echt parallel (kein gemeinsamer Punkt).")
    else:
        st.write("Die Richtungsvektoren sind nicht parallel.")
        
        # Gleichungssystem für Schnittpunkt aufstellen
        st.subheader("3. Schnittpunktberechnung")
        st.write("Setzen wir die Geradengleichungen gleich:")
        eq1 = Eq(g1[0] + t * r1[0], g2[0] + s * r2[0])
        eq2 = Eq(g1[1] + t * r1[1], g2[1] + s * r2[1])
        eq3 = Eq(g1[2] + t * r1[2], g2[2] + s * r2[2])
        
        st.latex(f"\\begin{{cases}} {latex(eq1)} \\\\ {latex(eq2)} \\\\ {latex(eq3)} \\end{{cases}}")
        
        # Lösen des Gleichungssystems (nur zwei Gleichungen nötig, wenn nicht parallel)
        try:
            sol = solve((eq1, eq2), (t, s))
            if sol:
                t_val = sol[t]
                s_val = sol[s]
                
                # Prüfen, ob Lösung konsistent mit dritter Gleichung
                check_eq3 = g1[2] + t_val * r1[2] - (g2[2] + s_val * r2[2])
                st.latex(f"Überprüfung 3. Gleichung: {g1[2] + t_val * r1[2]} = {g2[2] + s_val * r2[2]}")
                
                if abs(check_eq3) < 1e-10:  # Numerische Genauigkeit
                    st.write("Die Geraden schneiden sich.")
                    schnittpunkt = g1 + t_val * r1
                    st.latex(f"Schnittpunkt: \\vec{{x}} = {latex(g1)} + {t_val} \\cdot {latex(r1)} = {latex(schnittpunkt)}")
                else:
                    st.write("Die Geraden sind windschief (kein Schnittpunkt, nicht parallel).")
            else:
                st.write("Die Geraden sind windschief (kein Schnittpunkt, nicht parallel).")
        except:
            st.write("Die Geraden sind windschief oder das Gleichungssystem ist nicht lösbar.")
