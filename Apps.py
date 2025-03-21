streamlit
numpy
pillow
easyocr
import streamlit as st
import numpy as np
import pytesseract
from PIL import Image

import streamlit as st
import numpy as np
import easyocr
from PIL import Image

# EasyOCR-Reader initialisieren (Deutsch & Englisch)
reader = easyocr.Reader(['de', 'en'])

def extract_text_from_image(image):
    """Texterkennung mit EasyOCR"""
    text = reader.readtext(np.array(image), detail=0)
    return " ".join(text)

st.title("Lagebeziehung von Geraden + OCR-Texterkennung")

# Hochladen eines Bildes
uploaded_file = st.file_uploader("Lade ein Bild mit Vektoren hoch", type=["png", "jpg", "jpeg"])

git add Apps.py
git commit -m "EasyOCR hinzugefügt"
git push

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)

    # OCR ausführen
    text = extract_text_from_image(image)
    st.write("Erkannter Text:", text)
    
# Funktion zur Berechnung der Lagebeziehung mit Rechenweg
def check_lagebeziehung(a1, b1, a2, b2):
    a1, b1, a2, b2 = np.array(a1), np.array(b1), np.array(a2), np.array(b2)
    rechenweg = "**Rechenweg:**\n\n"

    # Überprüfung auf Parallelität
    if np.linalg.matrix_rank(np.column_stack((b1, b2))) == 1:
        rechenweg += "1️⃣ Die Richtungsvektoren sind **linear abhängig**, die Geraden sind also **parallel**.\n"
        # Überprüfen, ob sie identisch sind (gleiche Richtung + Stützvektor auf derselben Linie)
        if np.linalg.matrix_rank(np.column_stack((b1, a2 - a1))) == 1:
            return "Die Geraden sind **identisch**.", rechenweg
        else:
            return "Die Geraden sind **parallel**, aber nicht identisch.", rechenweg

    rechenweg += "2️⃣ Die Richtungsvektoren sind **linear unabhängig**.\n"

    # Überprüfung auf Schnittpunkt
    A = np.column_stack((b1, -b2))
    try:
        # Lösen des linearen Gleichungssystems für den Schnittpunkt
        lambdas = np.linalg.solve(A, a2 - a1)
        schnittpunkt = a1 + lambdas[0] * b1
        rechenweg += f"✅ Die Geraden schneiden sich in **{schnittpunkt}**.\n\n"
        rechenweg += f"3️⃣ Berechnung des Schnittpunkts:\n"
        rechenweg += f"  λ1 = {lambdas[0]}\n"
        rechenweg += f"  λ2 = {lambdas[1]}\n"
        rechenweg += f"  Schnittpunkt = a1 + λ1 * b1 = {schnittpunkt}\n"
        return f"Die Geraden schneiden sich in {schnittpunkt}.", rechenweg
    except np.linalg.LinAlgError:
        rechenweg += "❌ Es gibt keinen Schnittpunkt. Die Geraden sind **windschief**.\n"
        return "Die Geraden sind **windschief**.", rechenweg

# Funktion zur Texterkennung aus einem Bild
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang="eng")  # OCR durchführen
    return text.strip()

# Setze den Pfad zu Tesseract, falls nötig (Windows-Beispiel)
# Passe den Pfad an, wenn du auf Windows arbeitest und Tesseract nicht im System-Pfad ist
# Für Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit UI
st.title("Lagebeziehung von zwei Geraden mit Stütz- und Richtungsvektoren")

st.write("Gib die Stütz- und Richtungsvektoren der beiden Geraden ein (z. B. `(1,2,3)` für Stützvektor und `(4,5,6)` für Richtungsvektor).")

# Initialisiere session_state für die Eingabefelder
if 'a1' not in st.session_state:
    st.session_state.a1 = "(0,0,0)"
if 'b1' not in st.session_state:
    st.session_state.b1 = "(1,1,1)"
if 'a2' not in st.session_state:
    st.session_state.a2 = "(1,1,1)"
if 'b2' not in st.session_state:
    st.session_state.b2 = "(1,-1,1)"

# Eingabefelder für Vektoren
a1 = st.text_input("Stützvektor der 1. Gerade (z. B. (1,2,3))", st.session_state.a1)
b1 = st.text_input("Richtungsvektor der 1. Gerade (z. B. (4,5,6))", st.session_state.b1)

a2 = st.text_input("Stützvektor der 2. Gerade (z. B. (7,8,9))", st.session_state.a2)
b2 = st.text_input("Richtungsvektor der 2. Gerade (z. B. (10,11,12))", st.session_state.b2)

# Bild-Upload
uploaded_file = st.file_uploader("Bild mit Stütz- und Richtungsvektoren hochladen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)

    # OCR ausführen
    text = extract_text_from_image(image)
    st.write("Erkannter Text:", text)

    # Falls Stütz- und Richtungsvektoren erkannt wurden, automatisch in die Eingabefelder setzen
    equations = text.split("\n")
    equations = [eq.strip() for eq in equations if eq.strip()]
    if len(equations) >= 4:
        st.session_state.a1 = equations[0]
        st.session_state.b1 = equations[1]
        st.session_state.a2 = equations[2]
        st.session_state.b2 = equations[3]
        st.text_input("Stützvektor 1. Gerade (aus Bild erkannt)", st.session_state.a1)
        st.text_input("Richtungsvektor 1. Gerade (aus Bild erkannt)", st.session_state.b1)
        st.text_input("Stützvektor 2. Gerade (aus Bild erkannt)", st.session_state.a2)
        st.text_input("Richtungsvektor 2. Gerade (aus Bild erkannt)", st.session_state.b2)

# Berechnungs-Button
if st.button("Berechnen"):
    try:
        # Konvertiere die Eingabe in Vektoren
        a1 = np.array(eval(st.session_state.a1))
        b1 = np.array(eval(st.session_state.b1))
        a2 = np.array(eval(st.session_state.a2))
        b2 = np.array(eval(st.session_state.b2))

        result, rechenweg = check_lagebeziehung(a1, b1, a2, b2)
        st.success(result)
        st.markdown(rechenweg)

    except Exception as e:
        st.error(f"Fehler bei der Eingabe: {e}")
