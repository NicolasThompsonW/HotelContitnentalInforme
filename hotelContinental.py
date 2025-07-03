import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuración inicial ---
st.set_page_config(page_title="Informe Hotel Continental", layout="centered")
st.title("📊 Informe Preliminar: Hotel Continental")

# --- Introducción ---
st.markdown("""
### 📝 Introducción
Este informe es un análisis preliminar de las reseñas públicas del Hotel Continental.

Se busca identificar patrones de satisfacción e insatisfacción en diferentes áreas del servicio
y establecer posibles recomendaciones para mejorar la percepción general del hotel.
""")

# --- Datos reales del informe original ---
# Negativos: 12 totales (Cocina 9, Hotel 2, Mixto 1); Positivos: 8 (Hotel)
data = {
    "Categoría": [
        *["Cocina"]*9,
        *["Hotel"]*2,
        *["Mixto"]*1,
        *["Hotel"]*8
    ],
    "Sentimiento": [
        *["Negativo"]*12,
        *["Positivo"]*8
    ]
}
df = pd.DataFrame(data)

# --- Gráfico de barras: positivos y negativos por categoría ---
st.subheader("📊 Comentarios por Área y Sentimiento")
pivot = df.groupby(["Categoría", "Sentimiento"]).size().unstack(fill_value=0)
# Asegurar orden de categorías
pivot = pivot.reindex(index=["Hotel", "Cocina", "Mixto"])
fig, ax = plt.subplots(figsize=(8,5))
pivot.plot(kind="bar", stacked=True, colormap="Set2", ax=ax)
ax.set_title("Comentarios Positivos y Negativos por Categoría")
ax.set_xlabel("Categoría")
ax.set_ylabel("Cantidad de comentarios")
ax.tick_params(axis='x', rotation=0)
st.pyplot(fig)

# --- Gráfico circular: origen de comentarios negativos ---
st.subheader("📌 Distribución porcentual de comentarios negativos")
df_neg = df[df["Sentimiento"]=="Negativo"]
neg_counts = df_neg["Categoría"].value_counts().reindex(["Cocina","Hotel","Mixto"], fill_value=0)
fig2, ax2 = plt.subplots()
ax2.pie(
    neg_counts, labels=neg_counts.index, autopct="%1.1f%%", startangle=90,
    colors=sns.color_palette("Set2")
)
ax2.axis('equal')
ax2.set_title("Origen de Comentarios Negativos")
st.pyplot(fig2)

# --- Comparación con la competencia ---
st.subheader("📉 Comparación con la competencia")
st.markdown("""
En comparación con hoteles de categoría similar en la zona, el Hotel Continental presenta una calificación general menor,
principalmente afectada por los comentarios negativos vinculados a la cocina.

Mientras que el Gran Hotel Cosquín y el Hotel Casablanca tienen mejores reseñas y mayor actividad en redes,
el Hotel Continental muestra debilidades en su servicio gastronómico y presencia digital.
""")

# --- Tabla de calificaciones comparadas ---
st.subheader("📌 Calificaciones generales (competencia real)")
competencia = pd.DataFrame({
    "Hotel": ["Hotel Continental","Gran Hotel Cosquín","Hotel Casablanca"],
    "Google Reviews": [3.8,4.6,4.0],
    "TripAdvisor": [3.1,None,None],
    "Web & Redes": [
        "Sitio estático, redes limitadas",
        "Web moderna, IG activo @granhotelcosquin",
        "Sin web, IG activo @cosquincasablancahotel"
    ]
})
st.dataframe(competencia)

# --- Conclusiones ---
st.subheader("🔍 Conclusiones preliminares")
st.markdown("""
- El **75% de los comentarios negativos** están relacionados con la **cocina**.
- Problemas más frecuentes: **tiempos de espera**, **errores en pedidos**, **comida fría** y **falta de profesionalismo del personal**.
- El **17%** corresponde a críticas sobre las **habitaciones o servicios del hotel**.
- El **8% restante** son comentarios mixtos entre diferentes áreas.
- Los competidores analizados tienen una presencia web superior y un mayor engagement en redes.

### ✅ Recomendaciones:
- Auditar internamente el servicio de cocina y establecer protocolos claros.
- Capacitar al personal en atención, presentación y resolución de conflictos.
- Actualizar el sitio web con funciones modernas (reservas, diseño responsive).
- Diseñar una estrategia de contenido para redes sociales con enfoque en experiencia del cliente.
""")
# --- Cierre ---
st.subheader("📌 Notas finales")
st.markdown("""
Este informe forma parte de un estudio exploratorio que puede ampliarse
con análisis de competencia, datos históricos y encuestas directas a clientes.
""")
