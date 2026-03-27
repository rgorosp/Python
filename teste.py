"""
"""
import pandas as pd
dados = pd.DataFrame({
    'nota1': [5, 6, 7, 8, 3, 4, 9, 10, 6],
    'nota2': [6, 5, 8, 9, 2, 3, 10, 9, 7],
    'frequencia': [80, 90, 95, 98, 50, 60, 100, 40, 99],
    'aprovado': [1, 1, 1, 1, 0, 0, 1, 0, 1]
})

print(dados) 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = dados[['nota1', 'nota2', 'frequencia']]
y = dados['aprovado']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
from sklearn.metrics import accuracy_score

acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia:.2f}")

print("Predições:", y_pred)

print("Probabilidades de aprovação:", modelo.predict_proba(X_test)[:, 1])

print('------------------------------------------------------')

