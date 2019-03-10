import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import base64
import seaborn as sns
import pandas as pd
import io
import csv
from pprint import pprint
import math
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import plotly
plotly.tools.set_credentials_file(username='<your-plotly-username-here>', api_key='<your-plotly-api-key-here>')
import plotly.plotly as py
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as opy

# P = Product name 
# m = month

def analysis_destination(P,m,e,data='SIH.csv'):
    
    dataset=pd.read_csv(data)  
    x1=dataset.loc[(dataset['Product_Name']==P) & (dataset['Month']==m)]
    y1=x1.groupby('Day').sum()
    y=y1.iloc[:,2].values
    x=x1.iloc[::4, 4].values

    #place wise anlysis
    des=x1.loc[x1['Destination']==e]

    xp=des.iloc[:, 4].values
    yp=des.iloc[:, 5].values

    plt.figure()
    plt.bar(xp,yp,color='darkred')

    axes=plt.gca()
    axes.set_ylim([0,4000])
    plt.title('Destination of Supply Demand Analysis')
    plt.xlabel('Day')
    plt.ylabel('Quantity demanded')

    fig = plt.gcf()
    
    plotly_fig = tls.mpl_to_plotly(fig)

    plotly_fig['layout']['width'] = 1200
    plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)
    
    return plot_div

#seasonal analysis    
def analysis_seasonal(P,data='SIH.csv'):
    dataset=pd.read_csv(data)  
    
    x3=dataset.loc[dataset['Product_Name']==P]
    ses=x3.groupby('Month').sum()
    ses=ses.rename(columns={'Day':'month'})
    ses.month=range(0,12)
    ses['month']=ses['month']+1
    xs=ses.iloc[:,1]
    ys=ses.iloc[:,2]
    
    plt.figure()
    plt.xticks(xs)
    plt.bar(xs,ys,color='darkblue')
    plt.title('Monthly Demand')
    plt.xlabel('Month')
    plt.ylabel('Quantity demanded')

    fig = plt.gcf()
    
    plotly_fig = tls.mpl_to_plotly(fig)

    plotly_fig['layout']['width'] = 1200
    # py.iplot(plotly_fig, filename='mpl-basic-bar')
    plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

    return plot_div

def creategraph(product,typeofgraph,filename='SIH2.csv'):
    data=pd.read_csv(filename)
    c={}
    c['Year']=data['Year'].values
    c['Month']=data['Month'].values
    c['Day']=data['Day'].values
    for i in range(192):
        c['date']=str(c['Year'][i])+'-'+str(c['Month'][i])+'-'+str(c['Day'][i])
    d=pd.DataFrame(c)
    d=d.drop('Year',axis=1)
    d=d.drop('Month',axis=1)
    d=d.drop('Day',axis=1)
    data['date']=pd.to_datetime(d['date'],infer_datetime_format=True)
    y=['Profit']
    datay=data[y]
    

    if typeofgraph=='Quantity Demanded':

        #prediction of Quantity_Demanded mean monthly of A
        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Quantity_Demanded'],color='lightblue')
        plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Quantity Demanded mean monthly of '        

    if typeofgraph=='Labour Wages':

        #prediction of Labour Wages mean monthly
        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Labour_wages'])
        plt.plot(data['Month'].unique(),demA['Labour_wages'],color='red')
        fig=plt.gcf()
        
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Labour Wages mean monthly'
        
    if typeofgraph=='R and D':

        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['R_N_D'])
        plt.plot(data['Month'].unique(),demA['R_N_D'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of R&D cost monthly'

    if typeofgraph=='Energy':

        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Energy_cost'])
        plt.plot(data['Month'].unique(),demA['Energy_cost'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Energy Costs monthly'

    if typeofgraph=='Taxes':

        #prediction of Taxes mean monthly
        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Taxes'])
        plt.plot(data['Month'].unique(),demA['Taxes'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Taxes mean monthly'

    if typeofgraph=='Transport':

        #prediction of Transport mean monthly
        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Transport'])
        plt.plot(data['Month'].unique(),demA['Transport'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Transport mean monthly'

    if typeofgraph=='Production':

        #prediction of Production mean monthly
        x1=data.loc[data['Product_Name']==product]
        demA=x1.groupby('Month').mean()
        plt.figure()
        plt.bar(data['Month'].unique(),demA['Production'])
        plt.plot(data['Month'].unique(),demA['Production'],color='red')
        fig=plt.gcf()
        plotly_fig = tls.mpl_to_plotly(fig)
        plotly_fig['layout']['width'] = 1200
        plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)

        head = 'Prediction of Production mean monthly'

    pprint(plotly_fig)
    return plot_div, head


def profitloss(product,filename='SIH2.csv'):

    dataset=pd.read_csv(filename)
    x_1=dataset.loc[dataset['Product_Name']==product]
    ses1=x_1.groupby('Month').sum()
    ses1=ses1.rename(columns={'Day':'month'})
    ses1.month=range(0,12)
    ses1['month']=ses1['month']+1
    x_11=ses1.iloc[:,1]
    y_11=ses1.iloc[:,11]
    colorbar=[]
    for i in range(1,len(y_11)+1):
        if (y_11[i]<0):
            colorbar.append('red')
        else:
            colorbar.append('lightblue')
    plt.bar(x_11, abs(y_11), color=colorbar)
    
    plt.title('Profit/Loss, month-wise')
    blue_patch = mpatches.Patch(color='lightblue', label='Profit')
    red_patch = mpatches.Patch(color='red', label='Loss')
    plt.legend(handles=[blue_patch,red_patch])
    fig=plt.gcf()
    plotly_fig = tls.mpl_to_plotly(fig)
    plotly_fig['layout']['width'] = 1200
    plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)
    pprint(plotly_fig)

    return plot_div