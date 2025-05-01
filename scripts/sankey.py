import plotly.graph_objects as go
import plotly.io as pio

pio.kaleido.scope.default_format = "png"
pio.kaleido.scope.default_width = 2000   # adjust as desired
pio.kaleido.scope.default_height = 1200  # adjust as desired
pio.kaleido.scope.default_scale = 3      # 3× resolution

labels = [
    "Consumer", "Institutions",
    "Stablecoin", "Blockchain rewards", "Custodial fee", "Interest income", "Other sub",
    "Transaction-based", "Subscription & Services", "Other rev",
    "Revenue",
    "Operating profit", "Operating expenses",
    "Technology", "G&A", "Transaction", "S&M", "Other opex",
    "Tax", "Other profit",
    "Net profit"
]
idx = {lab: i for i, lab in enumerate(labels)}

sources = [
    idx["Consumer"], idx["Institutions"],
    idx["Stablecoin"], idx["Blockchain rewards"], idx["Custodial fee"],
    idx["Interest income"], idx["Other sub"],
    idx["Transaction-based"], idx["Subscription & Services"], idx["Other rev"],
    idx["Revenue"], idx["Revenue"],
    idx["Operating profit"], idx["Tax"], idx["Other profit"],
    idx["Operating expenses"], idx["Operating expenses"], idx["Operating expenses"],
    idx["Operating expenses"], idx["Operating expenses"]
]
targets = [
    idx["Transaction-based"], idx["Transaction-based"],
    idx["Subscription & Services"], idx["Subscription & Services"], idx["Subscription & Services"],
    idx["Subscription & Services"], idx["Subscription & Services"],
    idx["Revenue"], idx["Revenue"], idx["Revenue"],
    idx["Operating profit"], idx["Operating expenses"],
    idx["Net profit"], idx["Net profit"], idx["Net profit"],
    idx["Technology"], idx["G&A"], idx["Transaction"],
    idx["S&M"], idx["Other opex"]
]
values = [
    493, 37,
    172, 95, 43, 20, 47,
    529, 376, 49,
    116, 838,
    116, 141, 36,
    323, 281, 126, 106, 2
]

node_colors = (
    ["#FFFFFF"]*7 +
    ["#0052FF"]*4 + ["#0052FF"] +
    ["#00BA38", "#FF4C4C"] + ["#FF4C4C"]*5 +
    ["#D62828", "#00BA38"] + ["#00BA38"]
)
node_x = [0.0]*7 + [0.2]*3 + [0.4] + [0.6]*2 + [0.8]*5 + [0.6]*2 + [1.0]

fig = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        label=labels,
        color=node_colors,
        pad=35,
        thickness=5,
        line=dict(color='rgba(0,0,0,0)', width=0),
        x=node_x
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color='rgba(0, 84, 255, 0.15)'
    ),
    textfont=dict(color='#ebf1fa', size=24, family='Verdana'),
))

fig.update_layout(
    paper_bgcolor='#0e0e10',
    plot_bgcolor='#0e0e10',
    margin=dict(l=40, r=40, t=40, b=40),
    width=2000,
    height=1200
)

fig.write_image("../output/sankey_highres.png")

fig.show()