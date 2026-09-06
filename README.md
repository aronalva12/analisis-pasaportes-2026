# 🛂 Análisis de Emisión de Pasaportes Electrónicos (2026)

Este repositorio contiene un script desarrollado en Python utilizando la librería **Pandas** para procesar, limpiar y analizar el volumen de emisión de pasaportes electrónicos. El objetivo principal es extraer indicadores clave de demanda espacial y distribución demográfica.

---

## 🚀 Tecnologías y Herramientas
* **Python** 🐍
* **Pandas** (para manipulación, agregación y filtrado de datos)
* **Git & GitHub** (para el control de versiones y despliegue del portafolio)

---

## 📊 Principales Hallazgos y Resultados del Análisis

1. **Concentración de la Demanda por Sede:**
   * La oficina de **Surco (Lima)** lidera de manera absoluta el volumen de emisión de pasaportes electrónicos (superando los 62,000 registros en el segmento femenino y cerca de 48,000 en el masculino).
   * Le siguen en importancia operativa la sede central de **Lima** y **MAC Lima Norte**.

2. **Perfil Demográfico:**
   * La mayor parte de la demanda se concentra en el grupo de **mayores de edad (18 años a más)**.
   * Se observa una ligera predominancia del público femenino frente al masculino en las solicitudes procesadas.

3. **Auditoría y Calidad de Datos:**
   * Tras la validación de valores nulos mediante el análisis exploratorio, el dataset presentó **cero valores vacíos**, lo que garantiza una alta confiabilidad para la toma de decisiones.

---

## 💻 Código Destacado
El script realiza una lectura optimizada utilizando un delimitador personalizado (`|`) y aplica agrupamientos múltiples (`groupby`) con ordenamientos dinámicos:

```python
import pandas as pd

# Lectura del dataset con delimitador '|'
data = pd.read_csv(r"C:\Users\LENOVO\Documents\PASAPORTE ELECTRONICO 2026.csv", sep='|')

# Análisis agrupado por Sede, Departamento y Sexo
resumen_sedes = data.groupby(['DEPARTAMENTO_ATENCION', 'SEDE_ATENCION', 'SEXO'])['CANTIDAD'].sum().reset_index()
resumen_ordenado = resumen_sedes.sort_values(by='CANTIDAD', ascending=False)
print(resumen_ordenado)```