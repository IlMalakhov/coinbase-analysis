import plotly.graph_objects as go
import pandas as pd

# hard-coded but what can you do
data = [
    {"Year": 2012, "Event": "Founded by Brian Armstrong and Fred Ehrsam"},
    {"Year": 2012, "Event": "Launched buy/sell Bitcoin via bank transfers"},
    {"Year": 2013, "Event": "Secured $5M Series A funding"},
    {"Year": 2014, "Event": "Reached 1M users, added cold storage"},
    {"Year": 2015, "Event": "Launched Coinbase Exchange (later GDAX)"},
    {"Year": 2016, "Event": "Added Ethereum support, rebranded GDAX to Coinbase Pro"},
    {"Year": 2017, "Event": "Received BitLicense from NYDFS"},
    {"Year": 2018, "Event": "Launched Coinbase Custody, Wallet, USDC"},
    {"Year": 2019, "Event": "Launched Coinbase Prime & Card (UK)"},
    {"Year": 2020, "Event": "Expanded staking (Tezos), went remote-first"},
    {"Year": 2021, "Event": "Public listing on NASDAQ (COIN)"},
    {"Year": 2022, "Event": "Sunset Coinbase Pro, launched Advanced Trade"},
    {"Year": 2023, "Event": "Launched Base (L2), DeFi integrations"},
    {"Year": 2024, "Event": "Launched OnchainKit, 0-fee USDC ramps"},
    {"Year": 2025, "Event": "First AI Hackathon, expanded Ventures"},
]
df = pd.DataFrame(data)

# assign cascading y offsets for a cool waterfall effect: 1, –1, 2, –2, 3, –3, …
df['y'] = [((i // 2) + 1) * (1 if i % 2 == 0 else -1) for i in range(len(df))]

fig = go.Figure()

# central axis dots
fig.add_trace(go.Scatter(
    x=df['Year'], y=[0]*len(df),
    mode='markers',
    marker=dict(color='#0052FF', size=16),
    showlegend=False
))

# connectors + annotations
for year, y, text in zip(df['Year'], df['y'], df['Event']):
    # connector line
    fig.add_trace(go.Scatter(
        x=[year, year], y=[0, y],
        mode='lines',
        line=dict(color='rgba(255,255,255,0.3)', width=1),
        showlegend=False
    ))
    # annotation
    fig.add_annotation(
        x=year, y=y,
        text=text,
        showarrow=False,
        font=dict(color='rgba(255,255,255,0.7)', size=18, family='Verdana', weight='bold'),
        xanchor='center',
        yanchor='bottom' if y > 0 else 'top'
    )

fig.update_layout(
    plot_bgcolor='#0e0e10',
    paper_bgcolor='#0e0e10',
    xaxis=dict(
        tickmode='linear', dtick=1,
        showgrid=True, gridcolor='rgba(255,255,255,0.1)',
        color='rgba(255,255,255,0.5)',
        tickfont=dict(size=18)
    ),
    yaxis=dict(visible=False),
    margin=dict(l=60, r=60, t=100, b=60),
    showlegend=False,
    height=900,
    width=1800
)

# uncomment to export as png
# fig.write_image("output/coinbase_timeline_highres.png", scale=3)

fig.show()