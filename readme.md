# **Dashboard de Análisis de Internet**

## **Descripción del Proyecto**
Este proyecto tiene como objetivo analizar y visualizar datos relacionados con los accesos a internet, penetración por población y hogares, velocidades de conexión e ingresos generados por los servicios de internet. Utilizando un **Dashboard interactivo** desarrollado con **Streamlit**, el usuario puede explorar estos datos mediante gráficos dinámicos, filtros interactivos y estadísticas descriptivas.

El análisis se enfoca en:
- **Accesos por tecnología y localidad.**
- **Penetración de internet por población.**
- **Penetración de internet en hogares.**
- **Velocidad promedio de conexión por provincia.**
- **Ingresos generados por servicios de internet.**

## **Estructura del Proyecto**
El proyecto consta de los siguientes componentes:

### **1. EDA (Análisis Exploratorio de Datos)**
Se realiza una limpieza de datos inicial y una exploración para comprender mejor el contenido de los archivos y preparar los datos para el análisis. 

#### **Procesos del EDA:**
1. **Carga y Normalización de Datos:**
   - Los datos son cargados desde un archivo Excel llamado `Internet.xlsx` que contiene las siguientes hojas:
     - `Accesos_tecnologia_localidad`: Datos de accesos por tecnología y localidad.
     - `Penetración-poblacion`: Accesos por cada 100 habitantes por provincia.
     - `Penetracion-hogares`: Accesos por cada 100 hogares por provincia.
     - `Velocidad % por prov`: Velocidades promedio por provincia.
     - `Ingresos`: Ingresos generados por servicios de internet.
   - Los nombres de las columnas se normalizan eliminando caracteres especiales y espacios en blanco.

2. **Preparación de los Datos:**
   - Se reemplazan valores nulos en columnas de tipo texto con "Desconocido".
   - Los valores nulos en columnas numéricas se reemplazan por `0`.
   - Se realizan agrupaciones por categorías clave (tecnología, provincia, año, etc.) para calcular estadísticas descriptivas.

3. **Filtrado Dinámico:**
   - El EDA permite seleccionar años, provincias y tecnologías específicas para analizar los datos relevantes.

### **2. Dashboard Interactivo**
El Dashboard generado por el archivo `app.py` presenta los datos en diferentes secciones:

#### **1. Accesos por Tecnología**
- Muestra un gráfico de barras con los accesos totales para cada tecnología.
- Filtro interactivo para seleccionar tecnologías específicas desde el cuerpo principal.
- Tabla con los datos filtrados disponibles.

#### **2. Penetración por Población**
- Evolución temporal de la penetración de internet por cada 100 habitantes a lo largo de los años.
- Gráfico de barras con la penetración promedio por provincia.

#### **3. Penetración en Hogares**
- Gráfico de barras que muestra la penetración de internet en hogares por provincia y año seleccionado.

#### **4. Velocidad por Provincia**
- Histograma que muestra la distribución de las velocidades promedio de descarga por provincia.
- Métrica que calcula el porcentaje de provincias con velocidad promedio igual o superior a 30 Mbps.

#### **5. Ingresos por Servicios de Internet**
- Línea temporal que muestra el crecimiento anual de los ingresos generados por los servicios de internet.

#### **Conclusiones**
Un resumen interpretativo de los principales hallazgos, incluyendo:
1. Crecimiento en los accesos a internet.
2. Disparidades regionales en la penetración.
3. Velocidad promedio de conexión.
4. Tendencias en ingresos generados.

---

## **Requisitos del Proyecto**
### **Librerías Necesarias**
Asegúrate de tener instaladas las siguientes librerías antes de ejecutar el código:

```bash
pip install streamlit pandas plotly openpyxl
```

### **Estructura de Archivos**
El proyecto debe contener los siguientes archivos y carpetas:
```
📂 PROYECT_NAME/
├── app.py               # Código principal para ejecutar el dashboard
├── DATA/
│   └── Internet.xlsx    # Archivo Excel con los datos
└── README.md            # Archivo explicativo del proyecto
```

---

## **Ejecución del Proyecto**
1. **Clonar el Repositorio:**
   Clona este repositorio o descarga los archivos necesarios.

2. **Ejecutar el Dashboard:**
   En la terminal, navega hasta la carpeta que contiene `app.py` y ejecuta:

   ```bash
   streamlit run app.py
   ```

3. **Explorar el Dashboard:**
   Abre el enlace generado por Streamlit en tu navegador para explorar el dashboard interactivo.

---

## **Interacción en el Dashboard**
### **Filtros Interactivos**
- **Barra Lateral:**
  - Selección de año para análisis.
  - Selección de provincias específicas.
- **Cuerpo Principal:**
  - Filtro interactivo para seleccionar tecnologías específicas.

### **Visualizaciones Disponibles**
1. **Gráficos de Barras:**
   - Accesos por tecnología.
   - Penetración en población y hogares.
2. **Gráficos de Línea:**
   - Evolución temporal de la penetración de internet.
   - Crecimiento anual de ingresos.
3. **Histogramas:**
   - Distribución de velocidades promedio.

### **Datos Filtrados**
- Las tablas con los datos filtrados se muestran junto a los gráficos correspondientes para facilitar la interpretación.

---

## **Conclusiones Principales**
1. **Crecimiento Sostenido:** Los accesos a internet han crecido significativamente en los últimos años.
2. **Disparidades Regionales:** Algunas provincias tienen mayor penetración en comparación con otras, lo que indica desigualdad en el acceso.
3. **Conexiones Rápidas:** La mayoría de las provincias tienen velocidades de descarga aceptables, aunque algunas están por debajo del estándar deseado.
4. **Ingresos Variables:** Los ingresos por servicios de internet han mostrado un crecimiento inconsistente en los últimos años.

---

## **Contacto**
Si tienes preguntas o deseas contribuir, no dudes en contactarnos.
