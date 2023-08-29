## Readme

### Local Development

In order to run the api while developing, first you need to have the virtual environment set up. Then switch to the virtual env and go to the challenge folder and run the following command:

- `uvicorn api:app --reload`

### Deploy

The `cd.yml` file handles the deployment process to Google Cloud Run. Therefore, whenever code is pushed to the main branch, it triggers the deployment.

The URL of the API is the following: `https://latam-flight-service-prod-oedodimemq-uc.a.run.app`

### Eleccion del modelo:

Veamos una comparación más detallada de los informes de clasificación (classification_report) entre los dos modelos en cuestión: el XGBoost Classifier entrenado con Feature Importance y Balance de Clases (Modelo 6.b.i) y el Logistic Regression with Feature Importance and Balance (Modelo 6.b.iii). Luego, argumentaré en función de estos informes.

XGBoost Classifier entrenado con Feature Importance y Balance de Clases (Modelo 6.b.i):

|          | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
|     0    |    0.88   |  0.52  |   0.66   |  18294  |
|     1    |    0.25   |  0.69  |   0.37   |   4214  |
|----------|-----------|--------|----------|---------|
| Accuracy |           |        |   0.55   |  22508  |
|----------|-----------|--------|----------|---------|
|  Macro   |    0.56   |  0.61  |   0.51   |  22508  |
|   Avg    |    0.76   |  0.55  |   0.60   |  22508  |


Logistic Regression with Feature Importance and Balance (Modelo 6.b.iii):

|          | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
|     0    |    0.88   |  0.52  |   0.65   |  18294  |
|     1    |    0.25   |  0.69  |   0.36   |   4214  |
|----------|-----------|--------|----------|---------|
| Accuracy |           |        |   0.55   |  22508  |
|----------|-----------|--------|----------|---------|
|  Macro   |    0.56   |  0.61  |   0.51   |  22508  |
|   Avg    |    0.76   |  0.55  |   0.60   |  22508  |


Al observar los informes de clasificación, podemos notar que ambos modelos tienen resultados muy similares en términos de métricas de precisión, recall y f1-score. La precisión y recall para la clase 1 (demora) son consistentes en ambos modelos. La precisión en la clase 0 es alta en ambos casos, lo que indica que ambos modelos son buenos para predecir vuelos sin demoras.

En función de los informes de clasificación proporcionados y el rendimiento similar de los modelos, se podría elegir cualquiera de los dos modelos (6.b.i o 6.b.iii). Ambos parecen tener un rendimiento comparable en la tarea de predecir demoras en vuelos.

Sin embargo, yo eligiré el XGBoost Classifier with Feature Importance and Balance (Modelo 6.b.i).

Dado que las métricas de recall y precisión son iguales para ambos modelos y considerando la naturaleza del problema que se está abordando (predecir si un vuelo se retrasará o no), personalmente me inclinaría hacia el modelo XGBoost. A continuación, te proporciono mis razones:

- Flexibilidad: El modelo XGBoost tiene la capacidad de modelar relaciones no lineales y capturar patrones más complejos en los datos. Dado que los retrasos en los vuelos pueden estar influenciados por varios factores interconectados, esta flexibilidad podría ser beneficiosa.

- Potencial para mejoras futuras: Si en el futuro se necesita considerar más características o enfrentar datos más complejos, XGBoost puede ser más escalable y adaptable que la regresión logística. Además LATAM es una empresa grande con recursos, y se puede dar el lujo de gastar más recursos computacionales.

