import yfinance as yf
import plotly.express as px

df = yf.download("COIN", start="2021-04-14", end="2023-03-31", auto_adjust=False)
close = df["Close"].squeeze()

peak_date = close.idxmax()
peak_val  = close.max()
trough_date = close.idxmin()
trough_val  = close.min()
pct_drop = (peak_val - trough_val) / peak_val * 100

fig = px.area(x=close.index, y=close.values)
fig.update_traces(line_color="#0052FF", fillcolor="rgba(0,82,255,0.18)")

fig.add_shape(
    type="line",
    x0=peak_date, y0=peak_val,
    x1=trough_date, y1=trough_val,
    line=dict(color="#FAFAFA", width=1, dash="dot")
)

mid_date = peak_date + (trough_date - peak_date) / 2
mid_val  = peak_val  + (trough_val   - peak_val)   / 2

fig.add_annotation(
    x=mid_date, y=mid_val,
    text=f"{pct_drop:.1f}% drop",
    font=dict(color="#FAFAFA", size=40),
    showarrow=False,
    textangle=40
)

fig.update_layout(
    plot_bgcolor="#0e0e10",
    paper_bgcolor="#0e0e10",
    font_color="#FAFAFA",
    height=2160,
    width=4000,
    margin=dict(l=200, r=200, t=100, b=200)
)

fig.update_xaxes(
    title_text='',
    tickfont=dict(size=46, color="#FAFAFA"),
    showgrid=False,
    ticklabelstandoff=100,
    automargin=True
)
fig.update_yaxes(
    title_text='',
    tickfont=dict(size=46, color="#FAFAFA"),
    showgrid=False,
    ticksuffix="$",
    ticklabelstandoff=100,
    automargin=True,
    zeroline=False
)

fig.write_image("output/stock_drop.png", scale=1)
fig.show()