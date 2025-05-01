import plotly.graph_objects as go

# Data
quarters = [
    "Q1 2018", "Q2 2018", "Q3 2018", "Q4 2018",
    "Q1 2019", "Q2 2019", "Q3 2019", "Q4 2019",
    "Q1 2020", "Q2 2020", "Q3 2020", "Q4 2020",
    "Q1 2021", "Q2 2021", "Q3 2021", "Q4 2021",
    "Q1 2022", "Q2 2022", "Q3 2022", "Q4 2022",
    "Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023", "Q1 2024"
]
values = [
    2.7, 1.2, 0.9, 0.9,
    0.8, 1.3, 1.2, 1.0,
    1.3, 1.5, 2.1, 2.8,
    6.1, 8.8, 7.4, 11.4,
    9.2, 9.0, 8.5, 8.3,
    8.4, 7.3, 6.7, 7.0, 8.0
]

# find peak index and value
peak_idx = values.index(max(values))
peak_val = values[peak_idx]

fig = go.Figure()

# area + smooth line
fig.add_trace(go.Scatter(
    x=list(range(len(quarters))), y=values,
    mode='lines+markers',
    line=dict(shape='spline', width=3, color='#0052FF'),
    marker=dict(size=6, color='#0052FF'),
    fill='tozeroy',
    fillcolor='rgba(0,82,255,0.2)',
    hoverinfo='x+y'
))

# annotate peak value prominently
fig.add_annotation(
    x=peak_idx, y=peak_val + 1.0,
    text=f"{peak_val} M",
    showarrow=False,
    font=dict(color='grey', size=40, family='Verdana')
)

fig.update_layout(
    plot_bgcolor='#0e0e10',
    paper_bgcolor='#0e0e10',
    margin=dict(l=80, r=40, t=60, b=40),
    width=1920, height=540,
    xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
    yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
    showlegend=False
)

# uncomment to save
# fig.write_image("output/coinbase_users_top_slide.png", width=2560, height=540, scale=2)

fig.show()