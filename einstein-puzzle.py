# Mejoras al programa + README

Aquí está la versión mejorada del programa con ajustes visuales para que se vea aún más compacto y claro, y un archivo **README.md** con el instructivo para GitHub.

---

## 📄 Código mejorado (einstein_streamlit.py)

```python
import streamlit as st

st.set_page_config(page_title="Einstein Puzzle Checker", layout="wide")

HOUSES = [1, 2, 3, 4, 5]
NATIONALITIES = ["", "británico", "sueco", "danés", "noruego", "alemán"]
COLORS = ["", "roja", "verde", "blanca", "amarilla", "azul"]
BEVERAGES = ["", "té", "café", "leche", "cerveza", "agua"]
CIGARETTES = ["", "Prince", "Pall Mall", "Dunhill", "Blends", "Bluemaster"]
PETS = ["", "perro", "pájaros", "gato", "caballo", "pez"]

st.title("🐟 Acertijo de Einstein — Comprobador Interactivo")
st.caption("Completa la cuadrícula y verifica en tiempo real cuáles reglas se cumplen.")

if "state" not in st.session_state:
    st.session_state.state = {
        "nacionalidad": [""] * 5,
        "color": [""] * 5,
        "bebida": [""] * 5,
        "cigarro": [""] * 5,
        "mascota": [""] * 5,
    }

if st.button("🔄 Resetear"):
    st.session_state.state = {k: [""] * 5 for k in st.session_state.state}
    st.experimental_rerun()

# Compact layout
grid_col, rules_col = st.columns([2, 2])

with grid_col:
    st.subheader("Casas")
    cols = st.columns(5)
    for i, c in enumerate(cols):
        with c:
            st.markdown(f"### 🏠 {i+1}")
            st.session_state.state["nacionalidad"][i] = st.selectbox(
                "Nac.", NATIONALITIES, key=f"nac_{i}", label_visibility="collapsed"
            )
            st.session_state.state["color"][i] = st.selectbox(
                "Col", COLORS, key=f"col_{i}", label_visibility="collapsed"
            )
            st.session_state.state["bebida"][i] = st.selectbox(
                "Beb", BEVERAGES, key=f"bev_{i}", label_visibility="collapsed"
            )
            st.session_state.state["cigarro"][i] = st.selectbox(
                "Cig", CIGARETTES, key=f"cig_{i}", label_visibility="collapsed"
            )
            st.session_state.state["mascota"][i] = st.selectbox(
                "Masc", PETS, key=f"pet_{i}", label_visibility="collapsed"
            )

nac = st.session_state.state["nacionalidad"]
col = st.session_state.state["color"]
beb = st.session_state.state["bebida"]
cig = st.session_state.state["cigarro"]
pet = st.session_state.state["mascota"]

# Reglas
rules = []

def rule1():
    return any(nac[i] == "británico" and col[i] == "roja" for i in range(5))
rules.append(("1. Británico en la casa roja", rule1))

def rule2():
    return any(nac[i] == "sueco" and pet[i] == "perro" for i in range(5))
rules.append(("2. Sueco tiene perro", rule2))

def rule3():
    return any(nac[i] == "danés" and beb[i] == "té" for i in range(5))
rules.append(("3. Danés toma té", rule3))

def rule4():
    return nac[0] == "noruego"
rules.append(("4. Noruego en la 1ra casa", rule4))

def rule5():
    return any(nac[i] == "alemán" and cig[i] == "Prince" for i in range(5))
rules.append(("5. Alemán fuma Prince", rule5))

def rule6():
    return "verde" in col and "blanca" in col and col.index("verde") + 1 == col.index("blanca")
rules.append(("6. Verde a la izq. de Blanca", rule6))

def rule7():
    return "verde" in col and beb[col.index("verde")] == "café"
rules.append(("7. Verde bebe café", rule7))

def rule8():
    return "Pall Mall" in cig and pet[cig.index("Pall Mall")] == "pájaros"
rules.append(("8. Pall Mall cría pájaros", rule8))

def rule9():
    return "amarilla" in col and cig[col.index("amarilla")] == "Dunhill"
rules.append(("9. Amarilla fuma Dunhill", rule9))

def rule10():
    return beb[2] == "leche"
rules.append(("10. Casa central toma leche", rule10))

def rule11():
    return "Blends" in cig and ( \
        (cig.index("Blends")-1 >= 0 and pet[cig.index("Blends")-1] == "gato") or \
        (cig.index("Blends")+1 < 5 and pet[cig.index("Blends")+1] == "gato") )
rules.append(("11. Blends al lado de gato", rule11))

def rule12():
    return "caballo" in pet and ( \
        (pet.index("caballo")-1 >= 0 and cig[pet.index("caballo")-1] == "Dunhill") or \
        (pet.index("caballo")+1 < 5 and cig[pet.index("caballo")+1] == "Dunhill") )
rules.append(("12. Caballo al lado de Dunhill", rule12))

def rule13():
    return "Bluemaster" in cig and beb[cig.index("Bluemaster")] == "cerveza"
rules.append(("13. Bluemaster toma cerveza", rule13))

def rule14():
    return "Blends" in cig and ( \
        (cig.index("Blends")-1 >= 0 and beb[cig.index("Blends")-1] == "agua") or \
        (cig.index("Blends")+1 < 5 and beb[cig.index("Blends")+1] == "agua") )
rules.append(("14. Blends al lado de agua", rule14))

def rule15():
    return "noruego" in nac and "azul" in col and abs(nac.index("noruego") - col.index("azul")) == 1
rules.append(("15. Noruego al lado de azul", rule15))

with rules_col:
    st.subheader("Reglas")
    for text, fn in rules:
        ok = fn()
        color = "#2ecc71" if ok else "#e74c3c"
        icon = "✅" if ok else "✖"
        st.markdown(f"<div style='color:white; background-color:{color}; padding:4px; border-radius:4px; font-size:14px'>{text} {icon}</div>", unsafe_allow_html=True)

# Mostrar pista final
st.markdown("---")
if "pez" in pet:
    st.success(f"🐠 El pez está en la casa {pet.index('pez')+1}.")
else:
    st.info("🐠 Aún no se ha colocado el pez.")
```

---

## 📘 Archivo README.md

```markdown
# 🐟 Acertijo de Einstein — Interactivo con Streamlit

Este proyecto es una implementación del famoso **Acertijo de Einstein** en **Python + Streamlit**. Permite completar la cuadrícula de las 5 casas y comprobar en tiempo real si se cumplen las 15 reglas del enigma.

## 🚀 Características
- Interfaz interactiva en **Streamlit**.
- Cuadrícula de 5 casas con menús desplegables.
- Verificación automática de las 15 reglas.
- Colores: ✅ verde si la regla se cumple, ❌ rojo si no.
- Botón de **reset** para reiniciar la partida.
- Indicación final de dónde está el pez (si se coloca).

## 📦 Instalación
```bash
# Clonar repositorio
git clone https://github.com/tuusuario/einstein-puzzle
cd einstein-puzzle

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\\Scripts\\activate   # En Windows

# Instalar dependencias
pip install streamlit
```

## ▶️ Uso
Ejecuta el programa con:
```bash
streamlit run einstein_streamlit.py
```

Se abrirá en tu navegador una interfaz interactiva.

## 📚 Instructivo
1. Selecciona en cada casa la **nacionalidad, color, bebida, cigarro y mascota**.
2. A medida que completes, las **reglas se colorearán en verde o rojo**.
3. El objetivo es colocar todos los elementos de forma que las 15 reglas estén en verde.
4. Al final podrás identificar **quién tiene el pez**.

## 🎨 Capturas de pantalla
*(aquí puedes añadir capturas del programa corriendo en Streamlit)*

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.
```

---

👉 Ya tienes el código mejorado y el archivo **README.md** con el instructivo listo para subir a GitHub.  
¿Quieres que también genere ejemplos de **capturas simuladas** (imágenes de la interfaz) para ponerlas en el README?
