import plotly.express as px
import plotly.io as io
import pandas as pd
def plot_func():
    data = pd.read_csv("plotter/utils/lexington_max_loads_table.csv",index_col='Batteries (kWh)')
    #data = pd.read_json(df)

    fig = px.imshow(data,labels=dict(x="Panel Sizes (kW)", color="Load (kW"), origin='lower')
    fig.update_xaxes(side="bottom")
    fig.update_layout(
        title='Maximum Load for Battery/PV Panel Combos Based on Lexington PV Data',
        xaxis_nticks=36,
        autosize=False,
        width=1000,
        height=500)
    plot_div = io.to_html(fig, full_html=True)
    return plot_div

