import plotly.graph_objects as go

years = ["2019", "2020", "2021", "2022", "2023", "Q1 2024"]
values = [0.53373, 1.28, 7.84, 3.19, 3.11, 1.64]  # in billions

# find peak index and value
peak_idx = values.index(max(values))
peak_val = values[peak_idx]

fig = go.Figure()

# area + smooth line
fig.add_trace(go.Scatter(
    x=list(range(len(years))), y=values,
    mode='lines+markers',
    line=dict(shape='spline', width=3, color='#0052FF'),
    marker=dict(size=6, color='#0052FF'),
    fill='tozeroy',
    fillcolor='rgba(0,82,255,0.2)',
    hoverinfo='x+y'
))

# annotate peak revenue prominently
fig.add_annotation(
    x=peak_idx, y=peak_val + 1.0,
    text=f"{peak_val} B",
    showarrow=False,
    font=dict(color='grey', size=40, family='Verdana')
)

fig.update_layout(
    plot_bgcolor='#0e0e10',
    paper_bgcolor='#0e0e10',
    margin=dict(l=80, r=40, t=60, b=40),
    width=3300, height=540,
    xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
    yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
    showlegend=False
)

fig.write_image("../output/coinbase_revenue_top_slide.png", width=3300, height=540, scale=3)

fig.show()