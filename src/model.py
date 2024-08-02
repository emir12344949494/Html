# src/model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, roc_auc_score
import pandas as pd

def train_model():
    # Ejemplo: Cargar datos procesados
    X = pd.read_csv('data/processed/processed_data.csv')
    y = pd.read_csv('data/raw/datos.csv')['target']

    # Ejemplo: Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Ejemplo: Crear y entrenar el modelo (Random Forest)
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)

    # Ejemplo: Evaluar el modelo
    y_pred = rf_model.predict(X_test)
    y_pred_prob = rf_model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, y_pred))
    print('ROC AUC Score:', roc_auc_score(y_test, y_pred_prob))

if __name__ == "__main__":
    train_model()
