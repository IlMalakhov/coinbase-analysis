import plotly.graph_objects as go
import pandas as pd

# hard-coded but what can you do
data = [
    {"Year": 2012, "Event": "Founded by Brian Armstrong and Fred Ehrsam"},
    {"Year": 2012, "Event": "Launched buy/sell Bitcoin"},
    {"Year": 2013, "Event": "Secured $5M Series A funding"},
    {"Year": 2014, "Event": "Reached 1M users, added cold storage"},
    {"Year": 2015, "Event": "Launched Coinbase Exchange"},
    {"Year": 2016, "Event": "Added Ethereum support"},
    {"Year": 2017, "Event": "Received BitLicense"},
    {"Year": 2018, "Event": "Launched Coinbase Custody, Wallet, USDC"},
    {"Year": 2019, "Event": "Launched Coinbase Prime & Card"},
    {"Year": 2020, "Event": "Expanded staking (Tezos), went remote-first"},
    {"Year": 2021, "Event": "Public listing on NASDAQ"},
    {"Year": 2022, "Event": "Launched Advanced Trade"},
    {"Year": 2023, "Event": "Launched Base, DeFi integrations"},
    {"Year": 2024, "Event": "Launched OnchainKit"},
    {"Year": 2025, "Event": "First AI Hackathon, expanded Ventures"},
]

df = pd.DataFrame(data)

# assign cascading y offsets for a cool waterfall effect: 1, –1, 2, –2, 3, –3, …
df['y'] = [((i // 2) + 1) * (1 if i % 2 == 0 else -1) for i in range(len(df))]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Year'], y=[0]*len(df),
    mode='markers',
    marker=dict(color='rgba(22,82,240,0.3)', size=90),
    showlegend=False
))

# central axis dots
fig.add_trace(go.Scatter(
    x=df['Year'], y=[0]*len(df),
    mode='markers',
    marker=dict(color='#0052FF', size=50),
    showlegend=False
))

# connectors + annotations
for year, y, text in zip(df['Year'], df['y'], df['Event']):
    # connector line
    fig.add_trace(go.Scatter(
        x=[year, year], y=[0, y],
        mode='lines',
        line=dict(color='rgba(255,255,255,0.5)', width=3),
        showlegend=False
    ))
    # annotation
    fig.add_annotation(
        x=year, y=y,
        text=text,
        showarrow=False,
        font=dict(color='#FAFAFA', size=46, family='Courier New', weight='bold'),
        xanchor='center',
        yanchor='bottom' if y > 0 else 'top'
    )

fig.update_layout(
    plot_bgcolor='#0e0e10',
    paper_bgcolor='#0e0e10',
    xaxis=dict(
        tickmode='linear', dtick=1,
        showgrid=True, gridcolor='rgba(255,255,255,0.2)',
        color='rgba(255,255,255,0.7)',
        tickfont=dict(size=46)
    ),
    yaxis=dict(visible=False),
    margin=dict(l=60, r=60, t=100, b=60),
    showlegend=False,
    height=2160,
    width=3600
)

# uncomment to export as png
fig.write_image("output/coinbase_timeline_highres.png", scale=1)

fig.show()