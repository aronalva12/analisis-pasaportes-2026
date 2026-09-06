import pandas as pd

# Añade sep=';' para que detecte correctamente las columnas
data = pd.read_csv(r"C:\Users\LENOVO\Documents\PASAPORTE ELECTRONICO 2026.csv", sep='|')


#Analisis por Sede y Departamento

resumen_sedes = data.groupby(['DEPARTAMENTO_ATENCION','SEDE_ATENCION','SEXO'])['CANTIDAD'].sum().reset_index()
resumen_ordenado = resumen_sedes.sort_values(by='CANTIDAD', ascending=False)
print(resumen_ordenado)

#Agrupacion por edad
resumen_sex_edad = data.groupby(['SEXO','EDAD'])['CANTIDAD'].sum().reset_index()
resumen_sex_edad_ord = resumen_sex_edad.sort_values(by='CANTIDAD', ascending=False)
print(resumen_sex_edad_ord)

#Conteo de valores 
print(data['ESTADO_TRAMITE'].value_counts())


#Validacion de nulos
print(data.isnull())