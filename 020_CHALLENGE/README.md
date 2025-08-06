# Telecom X - Parte 2: Predicción de Cancelación de Clientes (Churn)

---

## Propósito del Análisis

El objetivo principal de este proyecto es **predecir la cancelación (churn) de clientes** en una empresa de telecomunicaciones utilizando variables relevantes extraídas de los datos históricos de los clientes.  
El análisis y modelado permiten anticipar qué clientes tienen mayor probabilidad de cancelar su contrato, proporcionando información clave para desarrollar estrategias efectivas de retención.



---

## Preparación de los Datos

### Clasificación de variables

- **Variables categóricas binarias:** Por ejemplo, `Churn` (Sí/No), `customer.gender` (Male/Female), `phone.PhoneService` (Yes/No).  
  Se codificaron a formato numérico 0/1 para que los modelos puedan procesarlas fácilmente.

- **Variables categóricas multiclase:** Ejemplos `internet.InternetService`, `account.Contract`, `account.PaymentMethod`.  
  Se transformaron con *One-Hot Encoding* para convertirlas en variables dummy binarias y evitar orden implícito.

- **Variables numéricas:** Como `customer.tenure`, `account.Charges.Monthly`, `account.Charges.Total`, `Total.Day`.  
  Estas variables fueron normalizadas con *StandardScaler* para estandarizar su escala después de dividir en entrenamiento y prueba.

### Etapas de preparación

1. **Limpieza:** Eliminación de filas con valores faltantes (`NaN`).
2. **Codificación:** Transformación de variables categóricas binarias y multiclase a variables numéricas.
3. **Separación:** División del dataset en conjuntos de entrenamiento y prueba (70% y 30%, respectivamente), manteniendo la proporción de clases mediante `stratify`.
4. **Normalización:** Escalado estándar aplicado solo al conjunto de entrenamiento, y luego transformado el conjunto de prueba con los mismos parámetros, para evitar fugas de información.

---

## Justificaciones de las decisiones tomadas

- La eliminación de filas con datos faltantes fue elegida para mantener la integridad del modelo, dado que el porcentaje de filas afectadas era bajo.  
- Usamos One-Hot Encoding para variables multiclase para evitar relaciones ordinales no deseadas en el modelo.  
- La división estratificada garantiza que la proporción de clientes que cancelan se preserve en ambos conjuntos, asegurando evaluación justa.  
- La normalización solo después del split evita la filtración de información — una buena práctica en machine learning.

---

## Análisis Exploratorio y Visualizaciones destacadas

Durante el Análisis Exploratorio de Datos (EDA), se identificaron insights clave mediante gráficos como:

- **Matriz de correlación:** para explorar relaciones entre variables numéricas y determinar cuáles tienen mayor asociación con la cancelación.  
- **Histogramas y boxplots:** para observar la distribución de cargos, tenure y otros factores entre clientes que cancelaron y que permanecen.  
- **Matriz de confusión:** para evaluar el desempeño de los modelos de Random Forest y Regresión Logística.  
- **Importancia de variables (Random Forest):** destacó que el tipo de contrato, antigüedad (tenure) y método de pago son los factores más determinantes para predecir churn.




