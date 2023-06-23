import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def plot_pareto(data, bar_x, bar_y, scatter_x, scatter_y, title_x, title_y, mean):
    pareto = px.bar(
        data,
        x=bar_x,
        y=bar_y,
        color=bar_x,
        color_discrete_sequence=px.colors.qualitative.T10,
        template='plotly_white',
        text_auto='.2s'
    )

    pareto.update_layout(
        width=800,
        height=600
    )

    pareto.add_scatter(
        x=data[scatter_x],
        y=data[scatter_y], 
        mode='lines+text',
        name='Porcentagem Acumulada',
        text=[f'{x:.2f}%' for x in data[scatter_y]],
        textposition='top center',
        yaxis='y2',
        line={'color': 'red'}
    )

    pareto.update_layout(
        xaxis=dict(title=title_x),
        yaxis=dict(title=title_y),
        yaxis2=dict(title='Porcentagem Acumulada', overlaying='y', side='right', showgrid=False, range=[0, 100])
    )

    pareto.update_traces(showlegend=False)
    pareto.add_shape(
        type='line',
        x0=0,
        x1=1,
        y0=80,
        y1=80,
        line=dict(color='white', width=1),
        xref='paper',
        yref='y2'
    )

    pareto.add_shape(
        type='line',
        x0=0,
        x1=7,
        y0=mean,
        y1=mean,
        line=dict(color='LightBlue', width=1)
    )

    pareto.add_annotation(
        x=4.5,
        y=mean,
        text= f"Média: {mean / 1000000:.2f}M",
        showarrow=True,
        arrowhead=1,
        ax=40,
        ay=-40,
        xref='x',
        font=dict(color='LightBlue')
    )

    return pareto

def plot_regressao_estimada(data, title, data_type, country_order=None):
    num_paises = math.ceil(len(data)/2)

    if country_order is not None:
        data = data.set_index('pais').loc[country_order].reset_index()

    regressao = make_subplots(rows=num_paises, cols=2, start_cell="bottom-left")
    regressao.update_layout(
        title=title,
        width=1300,
        height=600,
        showlegend=False,
        colorway = ['LightBlue', 'LightGreen', 'Orange', 'Lavender', 'Tan', 'Magenta', 'Cyan']
    )

    for i, pais in enumerate(data.pais):
        row = num_paises - (i // 2)
        col = (i % 2) + 1
        trace = go.Scatter(x=data.columns[1:], y=data.iloc[i, 1:], name=pais)
        x = np.array(data.columns[1:], dtype=data_type)
        y = np.array(data.iloc[i, 1:], dtype=data_type)
        coef = np.polyfit(x, y, 1)
        line = coef[1] + coef[0] * x
        reg = go.Scatter(x=x, y=line, mode='lines', name='Regressão', line=dict(color='red'))
        regressao.add_trace(reg, row=row, col=col)
        regressao.add_trace(trace, row=row, col=col)
        regressao.update_xaxes(
            title_text=pais,
            row=row,
            col=col,
            title_standoff=10,
            tickfont=dict(size=8),
            title_font=dict(size=10),
            tickvals=data.columns[1:]
        )

    return regressao