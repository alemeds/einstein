# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(layout="wide", page_title="Acertijo de Einstein")

st.title("🐠 Acertijo de Einstein – ¿Quién tiene el pez?")

st.write(
    "Completa la cuadrícula con las opciones correctas. "
    "Las reglas se validan en tiempo real: ✅ si se cumplen, ❌ si no."
)

houses = ["Casa 1", "Casa 2", "Casa 3", "Casa 4", "Casa 5"]
categories = ["Color", "Nacionalidad", "Bebida", "Cigarro", "Mascota"]

options = {
    "Color": ["", "roja", "verde", "blanca", "amarilla", "azul"],
    "Nacionalidad": ["", "británico", "sueco", "danés", "noruego", "alemán"],
    "Bebida": ["", "té", "café", "leche", "cerveza", "agua"],
    "Cigarro": ["", "Pall Mall", "Dunhill", "Prince", "Bluemaster", "Blends"],
    "Mascota": ["", "perro", "pájaro", "gato", "caballo", "pez"],
}

# Diccionarios para guardar selecciones
grid = {cat: {} for cat in categories}

# --- Diseño: dos columnas ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Cuadrícula de casas")

    # Encabezado de tabla
    header_cols = st.columns([1] + [1 for _ in houses])
    header_cols[0].markdown("**Categoría**")
    for i, h in enumerate(houses):
        header_cols[i+1].markdown(f"**{h}**")

    # Filas de categorías
    for cat in categories:
        row = st.columns([1] + [1 for _ in houses])
        row[0].markdown(f"**{cat}**")
        for i, h in enumerate(houses):
            grid[cat][i] = row[i+1].selectbox(
                "",
                options[cat],
                key=f"{cat}{i}",
                label_visibility="collapsed"
            )

with col2:
    st.subheader("Reglas")

    # Alias para accesibilidad
    col = grid["Color"]
    nac = grid["Nacionalidad"]
    beb = grid["Bebida"]
    cig = grid["Cigarro"]
    pet = grid["Mascota"]

    rules = []

    def rule1():
        return any(nac[i] == "británico" and col[i] == "roja" for i in range(5))
    rules.append(("1. El británico vive en la casa roja", rule1))

    def rule2():
        return any(nac[i] == "sueco" and pet[i] == "perro" for i in range(5))
    rules.append(("2. El sueco tiene un perro", rule2))

    def rule3():
        return any(nac[i] == "danés" and beb[i] == "té" for i in range(5))
    rules.append(("3. El danés toma té", rule3))

    def rule4():
        return nac[0] == "noruego"
    rules.append(("4. El noruego vive en la primera casa", rule4))

    def rule5():
        return any(nac[i] == "alemán" and cig[i] == "Prince" for i in range(5))
    rules.append(("5. El alemán fuma Prince", rule5))

    def rule6():
        return any(col[i] == "verde" and i < 4 and col[i + 1] == "blanca" for i in range(4))
    rules.append(("6. La casa verde está a la izquierda de la blanca", rule6))

    def rule7():
        return any(col[i] == "verde" and beb[i] == "café" for i in range(5))
    rules.append(("7. El dueño de la casa verde toma café", rule7))

    def rule8():
        return any(cig[i] == "Pall Mall" and pet[i] == "pájaro" for i in range(5))
    rules.append(("8. Pall Mall ↔ pájaros", rule8))

    def rule9():
        return any(col[i] == "amarilla" and cig[i] == "Dunhill" for i in range(5))
    rules.append(("9. Amarilla ↔ Dunhill", rule9))

    def rule10():
        return beb[2] == "leche"
    rules.append(("10. La casa del centro toma leche", rule10))

    def rule11():
        return any(
            cig[i] == "Blends" and (
                (i > 0 and pet[i - 1] == "gato") or (i < 4 and pet[i + 1] == "gato")
            )
            for i in range(5)
        )
    rules.append(("11. Blends junto a gato", rule11))

    def rule12():
        return any(
            pet[i] == "caballo" and (
                (i > 0 and cig[i - 1] == "Dunhill") or (i < 4 and cig[i + 1] == "Dunhill")
            )
            for i in range(5)
        )
    rules.append(("12. Caballo junto a Dunhill", rule12))

    def rule13():
        return any(cig[i] == "Bluemaster" and beb[i] == "cerveza" for i in range(5))
    rules.append(("13. Bluemaster ↔ cerveza", rule13))

    def rule14():
        return any(
            cig[i] == "Blends" and (
                (i > 0 and beb[i - 1] == "agua") or (i < 4 and beb[i + 1] == "agua")
            )
            for i in range(5)
        )
    rules.append(("14. Blends junto a agua", rule14))

    def rule15():
        return any(
            nac[i] == "noruego" and (
                (i > 0 and col[i - 1] == "azul") or (i < 4 and col[i + 1] == "azul")
            )
            for i in range(5)
        )
    rules.append(("15. Noruego junto a la casa azul", rule15))

    # Mostrar resultados
    for text, fn in rules:
        try:
            ok = fn()
        except Exception:
            ok = False
        color = "#2ecc71" if ok else "#e74c3c"
        icon = "✅" if ok else "❌"
        st.markdown(
            f"<div style='color:white; background-color:{color}; "
            f"padding:3px; margin:2px; border-radius:3px; font-size:13px'>{icon} {text}</div>",
            unsafe_allow_html=True
        )

st.markdown("---")
st.info("Pista: Solo uno de los dueños tiene un 🐠 pez. ¿Podés descubrir cuál?")
