''' Biểu đồ đo lường '''

import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number+delta",
    title = {'text': "Vận tốc xe"},
    delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 500]},
             'steps' : [
                 {'range': [0, 100], 'color': "red"},
                 {'range': [100, 250], 'color': "lightyellow"},
                 {'range': [250, 400], 'color': "lightgreen"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 1, 'value': 490}}))

fig.show()