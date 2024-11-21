import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Análisis de Internet", layout="wide")

# Título del Dashboard
st.title("Dashboard de Análisis de Internet")

# Carga de Datos
@st.cache_data
def cargar_datos():
    file_path = "DATA/Internet.xlsx"
    excel = pd.ExcelFile(file_path)
    df_accesos = excel.parse("Accesos_tecnologia_localidad")
    df_poblacion = excel.parse("Penetración-poblacion")
    df_hogares = excel.parse("Penetracion-hogares")
    df_velocidad = excel.parse("Velocidad % por prov")
    df_ingresos = excel.parse("Ingresos")
    return df_accesos, df_poblacion, df_hogares, df_velocidad, df_ingresos

df_accesos, df_poblacion, df_hogares, df_velocidad, df_ingresos = cargar_datos()

# Normalización de nombres de columnas
df_accesos.columns = df_accesos.columns.str.strip().str.replace('▒', 'ó', regex=False).str.replace(' ', '_')
df_poblacion.columns = df_poblacion.columns.str.strip().str.replace('▒', 'ó', regex=False).str.replace(' ', '_')
df_hogares.columns = df_hogares.columns.str.strip().str.replace('▒', 'ó', regex=False).str.replace(' ', '_')
df_velocidad.columns = df_velocidad.columns.str.strip().str.replace('▒', 'ó', regex=False).str.replace(' ', '_')
df_ingresos.columns = df_ingresos.columns.str.strip().str.replace('▒', 'ó', regex=False).str.replace(' ', '_')

# Barra Lateral para Filtros
st.sidebar.header("Filtros")

# Filtro por Año
anio_seleccionado = st.sidebar.selectbox(
    "Selecciona el Año",
    options=sorted(df_poblacion["Año"].unique())
)

# Filtro por Provincia
provincias = sorted(df_poblacion["Provincia"].unique())
provincia_seleccionada = st.sidebar.multiselect(
    "Selecciona la(s) Provincia(s)",
    options=provincias,
    default=provincias  # Seleccionar todas las provincias por defecto
)

# 1. Accesos por Tecnología con Interactividad
st.header("1. Accesos por Tecnología")

if "Tecnologia" in df_accesos.columns:
    # Agrupar datos por tecnología
    accesos_por_tecnologia = df_accesos.groupby("Tecnologia")["Accesos"].sum().reset_index()

    # **Mover el filtro de Tecnología aquí**
    tecnologias = accesos_por_tecnologia["Tecnologia"].unique()
    tecnologias_seleccionadas = st.multiselect(
        "Selecciona la(s) Tecnología(s):",
        options=tecnologias,
        default=tecnologias  # Seleccionar todas por defecto
    )

    # Filtrar datos según las tecnologías seleccionadas
    accesos_filtrados = accesos_por_tecnologia[accesos_por_tecnologia["Tecnologia"].isin(tecnologias_seleccionadas)]

    # Crear gráfico de barras con las tecnologías filtradas
    st.subheader("Accesos Totales por Tecnología (Filtrados)")
    fig1 = px.bar(accesos_filtrados, x="Tecnologia", y="Accesos",
                  title="Accesos Totales por Tecnología",
                  labels={"Accesos": "Total de Accesos"})
    st.plotly_chart(fig1, use_container_width=True)

    # Mostrar tabla de datos filtrados
    st.subheader("Datos Filtrados")
    st.dataframe(accesos_filtrados)
else:
    st.error("La columna 'Tecnologia' no se encuentra en el DataFrame. Verifica los datos.")

# 2. Penetración por Población
st.header("2. Penetración por Población")

df_poblacion_filtrado = df_poblacion[
    (df_poblacion["Año"] == anio_seleccionado) & (df_poblacion["Provincia"].isin(provincia_seleccionada))
]

st.subheader("Evolución Temporal de la Penetración de Internet")
penetracion_temporal = df_poblacion.groupby("Año")["Accesos_por_cada_100_hab"].mean().reset_index()
fig2 = px.line(penetracion_temporal, x='Año', y='Accesos_por_cada_100_hab',
               title="Evolución de la Penetración de Internet (Accesos por cada 100 habitantes)")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Penetración de Internet por Provincia")
penetracion_por_provincia = df_poblacion_filtrado.groupby("Provincia")["Accesos_por_cada_100_hab"].mean().reset_index()
fig3 = px.bar(penetracion_por_provincia, x='Provincia', y='Accesos_por_cada_100_hab',
             title="Penetración de Internet por Provincia (Promedio)",
             labels={"Accesos_por_cada_100_hab": "Accesos por cada 100 habitantes"},
             color='Accesos_por_cada_100_hab', color_continuous_scale='Blues')
st.plotly_chart(fig3, use_container_width=True)

# 3. Penetración en Hogares
st.header("3. Penetración en Hogares")

df_hogares_filtrado = df_hogares[
    (df_hogares["Año"] == anio_seleccionado) & (df_hogares["Provincia"].isin(provincia_seleccionada))
]

st.subheader("Penetración de Internet en Hogares por Provincia")
fig4 = px.bar(df_hogares_filtrado, x='Provincia', y='Accesos_por_cada_100_hogares',
             title="Penetración de Internet en Hogares (Por Año y Provincia)",
             labels={"Accesos_por_cada_100_hogares": "Accesos por cada 100 hogares"},
             color='Accesos_por_cada_100_hogares', color_continuous_scale='Greens')
st.plotly_chart(fig4, use_container_width=True)

# 4. Velocidad por Provincia
st.header("4. Velocidad por Provincia")

df_velocidad_filtrado = df_velocidad[df_velocidad["Provincia"].isin(provincia_seleccionada)]

st.subheader("Distribución de Velocidades Promedio de Descarga")
fig5 = px.histogram(df_velocidad_filtrado, x='Mbps_(Media_de_bajada)', nbins=20,
                   title="Distribución de Velocidades Promedio de Descarga (Mbps)",
                   labels={"Mbps_(Media_de_bajada)": "Mbps (Media de bajada)"})
st.plotly_chart(fig5, use_container_width=True)

# KPI: Porcentaje de provincias con velocidad >= 30 Mbps
provincias_30_mbps = df_velocidad_filtrado[df_velocidad_filtrado["Mbps_(Media_de_bajada)"] >= 30]["Provincia"].nunique()
total_provincias = df_velocidad_filtrado["Provincia"].nunique()
kpi_velocidad = (provincias_30_mbps / total_provincias) * 100
st.metric("Porcentaje de Provincias con Velocidad >= 30 Mbps", f"{kpi_velocidad:.2f}%")

# 5. Ingresos por Servicios de Internet
st.header("5. Ingresos por Servicios de Internet")

st.subheader("Incremento Anual en Ingresos")
df_ingresos["Crecimiento_Anual"] = df_ingresos["Ingresos_(miles_de_pesos)"].pct_change() * 100
fig6 = px.line(df_ingresos, x='Año', y='Crecimiento_Anual',
              title="Crecimiento Anual en Ingresos por Servicios de Internet",
              labels={"Crecimiento_Anual": "Crecimiento (%)"})
st.plotly_chart(fig6, use_container_width=True)

# Conclusiones
st.header("Conclusiones")
st.markdown("""
1. **Crecimiento de Accesos**: Se observa un crecimiento sostenido en el acceso a internet tanto por población como por hogares.
2. **Velocidad de Conexión**: La mayoría de las provincias han alcanzado velocidades promedio superiores a 30 Mbps, lo cual es positivo para la experiencia del usuario.
3. **Ingresos**: Aunque hay crecimiento en ingresos en años anteriores, se detecta una tendencia negativa en los últimos años.
4. **Disparidades Regionales**: Existen diferencias significativas en la penetración de internet entre provincias.
""")
