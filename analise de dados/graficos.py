#criação de gráficos

import plotly.express as px
import plotly.io as pio

# Força o uso do navegador como visualizador
pio.renderers.default = 'browser'

# Dados de exemplo
fig = px.bar(x=["Maçã", "Banana", "Laranja"], y=[10, 20, 15], title="Frutas")

# Mostra o gráfico
fig.show()