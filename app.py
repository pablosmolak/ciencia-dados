import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

data = pd.read_csv(url)

setosa = data[data['species'] == 'setosa']
virginica = data[data['species'] == 'virginica']
versicolor = data[data['species'] == 'versicolor']


# Exibição dos dados
st.write("### Dados de exemplo da flor Íris")
st.write(data)

st.write("Gráfico de Dispersão - Sepal")
fig, ax = plt.subplots()
ax.scatter(setosa["sepal_length"],setosa["sepal_width"], label="Setosa").set_color("#3498db")
ax.scatter(virginica["sepal_length"],virginica["sepal_width"], label="Virginica").set_color("#e74c3c")
ax.scatter(versicolor["sepal_length"],versicolor["sepal_width"], label = "Versicolor").set_color("#2ecc71")

ax.set_xlabel("Comprimento")
ax.set_ylabel("Largura")

ax.legend()

st.pyplot(fig)


st.write("Gráfico de Dispersão - Petal")
fig, ax = plt.subplots()
ax.scatter(setosa["petal_length"],setosa["petal_width"], label="Setosa").set_color("#3498db")
ax.scatter(virginica["petal_length"],virginica["petal_width"], label="Virginica").set_color("#e74c3c")
ax.scatter(versicolor["petal_length"],versicolor["petal_width"], label = "Versicolor").set_color("#2ecc71")

ax.set_xlabel("Comprimento")
ax.set_ylabel("Largura")

ax.legend()

st.pyplot(fig)

