import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


def plot_graph():
    path="/home/aditya/Documents/learn-django/django_app/django_app/extrastate.csv"
    data=pd.read_csv(path)
    data.head()
    data.shape
    print(data.columns)
    data=data.dropna()
    data['war_type'].unique()
    sns.countplot(x='war_type',data=data,palette='hls')
    # plt.show()
    
    fig = Figure()
    canvas = FigureCanvas(fig)
    buf = io.IOBytes()
    plot.savefig(buf, format='png')
    plt.close(fig)

    data['side1_code'].unique()
    data['side1_name'].unique()
    data['side2_code'].unique()
    data['start_year1'].unique()
    data['start_month1'].unique()
    data['start_day1'].unique()
    data['end_year1'].unique()
    data['end_month1'].unique()
    data['end_day1'].unique()
    data['start_year2'].unique()
    data['start_month2'].unique()
    data['start_day2'].unique()
    data['end_year1'].unique()
    data['end_month2'].unique()
    data['end_day2'].unique()
    data['previous_war'].unique()
    data['intervention'].unique()
    data['initiation'].unique()
    data['combat_location'].unique()
    data['state_fatalities'].unique()
    data['nonstate_fatalities'].unique()
    data['outcome'].unique()
    data['next_war'].unique()
    data=data.drop(['next_war','nonstate_fatalities','previous_war','end_day2','end_month2','start_day2','start_month2','start_year2'],axis=1)
    y=['war_type']
    cols=data.columns
    to_keep=[i for i in cols if i not in y]
    X=data[to_keep]

    #---------------------------------------------------------------------------------------

    plt.figure()
    pd.crosstab(data.war_type,X.outcome).plot(kind='bar')
    plt.legend()
    plt.title('First Plot')
    plt.show()

    #---------------------------------------------------------------------------------------
    
    plt.figure()
    pd.crosstab(data.war_type,X.side1_code).plot(kind='bar')
    plt.legend()
    plt.title('Second Plot')
    plt.show()

    return buf
