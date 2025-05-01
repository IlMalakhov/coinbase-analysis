import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Simulated 5-day performance data
np.random.seed(42)
exchanges = ["Coinbase", "Binance", "FTX", "Gemini", "Kraken", "Okex"]
means = [30, 0, 15, -5, -1, -3]
data = {ex: np.random.normal(loc=mu, scale=10, size=50) for ex, mu in zip(exchanges, means)}
df = pd.DataFrame(data)

colors = {
    "Coinbase": "#1652f0",
    "Binance": "#F0B90B",
    "FTX": "#33bbc7",
    "Gemini": "#00dcfa",
    "Kraken": "#5841D8",
    "Okex": "#8ddc97"
}

fig = go.Figure()

for exchange in exchanges:
    fig.add_trace(go.Box(
        y=df[exchange],
        name=exchange,
        boxpoints='outliers',
        marker_color=colors[exchange],
        fillcolor=colors[exchange],
        line=dict(width=3),
        opacity=1,
        showlegend=False
    ))

fig.add_shape(
    type="line", x0=-0.5, x1=5.5, y0=0, y1=0,
    line=dict(color="#0e0e10", width=2, dash="dash")
)

fig.update_layout(
    height=3800,
    width=4000,
    plot_bgcolor="#0e0e10",
    paper_bgcolor="#0e0e10",
    font=dict(family="Helvetica", size=40, color="#FAFAFA"),
    xaxis=dict(
        title="",
        showline=False,
        showgrid=False,
        color="#FAFAFA",
        tickfont=dict(size=90)
    ),
    yaxis=dict(
        title="",
        tickformat=".0f",   # format as integer
        ticksuffix="%",     # append a percent sign  
        gridcolor="rgba(255,255,255,0.1)",
        color="#FAFAFA",
        tickfont=dict(size=70),
    ),
    margin=dict(l=200, r=20, t=20, b=200),
    showlegend=False
    
)

fig.write_image("../output/coinbase_performance_dark.png", scale=3)

fig.show()