from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Leer tus archivos Excel con datos para gráficos interactivos
    df_max = pd.read_excel('./temperatura_maxima.xlsx')
    df_min = pd.read_excel('./temperatura_minima.xlsx')

    # Asegurar que las columnas sean: Estación, Temperatura
    df_max = df_max[['Estación', 'Temperatura']].sort_values(by='Temperatura', ascending=False)
    df_min = df_min[['Estación', 'Temperatura']].sort_values(by='Temperatura', ascending=True)


    # Gráfico interactivo 1: Temperatura Máxima
    fig1 = px.bar(df_max, x='Estación', y='Temperatura',
                  title='',
                  color='Estación',
                  labels={'Temperatura': '°C'})
    grafico_interactivo_1 = fig1.to_html(full_html=False)

    # Gráfico interactivo 2: Temperatura Mínima
    fig2 = px.bar(df_min, x='Estación', y='Temperatura',
                  title='',
                  color='Estación',
                  labels={'Temperatura': '°C'})
    grafico_interactivo_2 = fig2.to_html(full_html=False)

    return render_template("index.html",
                           grafico1=grafico_interactivo_1,
                           grafico2=grafico_interactivo_2)

# ⬇️ ESTA PARTE ES OBLIGATORIA PARA QUE FUNCIONE
if __name__ == '__main__':
    app.run(debug=True)




















