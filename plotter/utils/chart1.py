import plotly.express as px
import plotly.io as io
import pandas as pd
def plot_func():
    max_loads_table = pd.read_csv("plotter/utils/lexington_max_loads_table.csv",index_col='Batteries (kWh)')
    fig = px.imshow(max_loads_table,labels=dict(x="Panel Sizes (kW)", color="Load (kW"), origin='lower')
    fig.update_xaxes(side="bottom")
    fig.update_layout(
        title='Maximum Load for Battery/PV Panel Combos Based on Lexington PV Data',
        xaxis_nticks=36)
    plot_div = io.to_html(fig, full_html=True)
    return plot_div

    