from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('sleep.csv')

opcoes = list(df['Occupation'].unique())

app.layout = html.Div(children=[
    html.H1(children='Qualidade de Sono e Estilo de Vida'),

    html.H2(children='Um olhar adentro de métricas compreensíveis para qualidade de vida'),

    dcc.Dropdown(
        id='dropdown',
        options=[{'label': option, 'value': option} for option in opcoes],
        value=opcoes[0]
    ),

    dcc.Graph(
        id='stacked-bar-chart',
    )
])

@app.callback(
    Output('stacked-bar-chart', 'figure'),
    Input('dropdown', 'value')
)
def update_stacked_bar_chart(selected_occupation):
    filtered_df = df[df['Occupation'] == selected_occupation]

    fig = px.bar(filtered_df, x="Physical Activity Level", y="Quality of Sleep", color="Occupation", barmode="stack",
                 title=f'Correlação entre Atividade Física e Qualidade de Sono ({selected_occupation})')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
