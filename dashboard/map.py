import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import pandas as pd

def printmap():
    mapbox_access_token = 'pk.eyJ1IjoiYWRpdHlhMDk4NzY1NDMyMSIsImEiOiJjanNzbHZsNDcxb3A1NDlvNHdqa2lkbDhtIn0.bxa2ewJsYTyW_NJcShlPbw'

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')
    site_lat = df.lat
    site_lon = df.lon
    locations_name = df.text

    data = [
        go.Scattermapbox(
            lat=site_lat,
            lon=site_lon,
            mode='markers',
            marker=dict(
                size=17,
                color='rgb(255, 0, 0)',
                opacity=0.7
            ),
            text=locations_name,
            hoverinfo='text'
        ),
        go.Scattermapbox(
            lat=site_lat,
            lon=site_lon,
            mode='markers',
            marker=dict(
                size=8,
                color='rgb(242, 177, 172)',
                opacity=0.7
            ),
            hoverinfo='none'
        )]
            
    layout = go.Layout(
        title='Sales of products',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38,
                lon=-94
            ),
            pitch=0,
            zoom=3,
            style='light'
        ),
    )

    fig = dict(data=data, layout=layout)
    plotmap = py.plot(fig, filename='Nuclear Waste Sites on American Campuses', auto_open=False)
    return plotmap