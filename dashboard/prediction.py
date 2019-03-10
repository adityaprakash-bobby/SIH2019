import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64
import seaborn as sns
import pandas as pd
import io
import csv
from pprint import pprint

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import plotly
plotly.tools.set_credentials_file(username='<your-plotly-username-here>', api_key='<your-plotly-api-key-here>')
import plotly.plotly as py
import plotly.tools as tls
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as opy

from statsmodels.tsa.ar_model import AR

def returnpred(p,m,file='SIH.csv'):
    dataset=pd.read_csv(file)
    x1=dataset.loc[(dataset['Product_Name']==p) & (dataset['Month']==m)]
    y1=x1.groupby('Day').mean()
    y1=y1.rename(columns={'Month':'days'})
    y=y1.iloc[:,5]
    n1=len(y)
    train1=y[0:25]
    test1=y[25:n1]
    model_AR=AR(train1)
    model_fit_AR=model_AR.fit()
    predictions_AR=model_fit_AR.predict(start=25,end=n1+10)
    
    plt.figure()
    plt.plot(test1)
    plt.plot(predictions_AR,color='red')
    plt.title("Future Predictions of different company")
    plt.legend(['Original','Predictions'])
    
    fig=plt.gcf()
    plotly_fig = tls.mpl_to_plotly(fig)
    plotly_fig['layout']['width'] = 1200
    plot_div = plot(plotly_fig, output_type='div', include_plotlyjs=False)
    return plot_div

def returnAR(P,m,day,dataset='SIH.csv'):
    dataset=pd.read_csv(dataset)
    #importing the dataset
    x1=dataset.loc[(dataset['Product_Name']==P) & (dataset['Month']==m)]
    y1=x1.groupby('Day').sum()
    #y1.drop(y1.columns[[0,3,4,5,6,7,8]], axis=1, inplace=True)
    #y1['Month']=range(31)
    y1_diff= y1.diff(periods=1)
    y1_diff= y1[1:]
    y1_diff.head()  
    #x=y1.iloc[:, 1].values
    y=y1.iloc[:, 2].values
    n1=len(y)
    train1=y[0:25]
    test1=y[25:n1]
    model_AR=AR(train1)
    model_fit_AR=model_AR.fit()
    predictions_AR= model_fit_AR.predict(start=25,end=n1+day)
    
    #pyplot

    plt.figure()
    plt.xlabel('Days')
    plt.ylabel('Quantity Demanded')
    plt.title('Future Predictions')
    plt.legend().remove()
    plt.plot(test1,label="Actual")
    plt.plot(predictions_AR,color='red',label="Predicted")
    axes=plt.gca()
    axes.set_ylim([1000,5000])
    plt.legend()
    plt.show()

    fig=plt.gcf()
    plotly_fig=tls.mpl_to_plotly(fig)

    # plotly config
    plotly_fig['layout']['width'] = 600
    plot_div_AR = plot(plotly_fig, output_type='div', include_plotlyjs=False)
    return plot_div_AR

def graphs1(file="SIH2_1.csv"):
    sns.set(style='whitegrid',color_codes=True)
    path=file
    data=pd.read_csv(path)
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

    data.head()
    y=['Profit']
    datay=data[y]
    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[(data['Company_Name']=='A')]
    demA=x1.groupby('Month').mean()
    #max=demA[demA['Quantity_Demanded']==demA['Quantity_Demanded'].max()]
    #sub1.bar(data['Month'].unique(),demA['Quantity_Demanded'])
    
    plt.figure()
    
    
    plt.xlabel('Month')
    plt.ylabel('Quantity Demanded')
    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='red',label='COMPANY A')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Company_Name']=='B']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='blue',label='COMPANY B')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Company_Name']=='C']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='green',label='COMPANY C')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Company_Name']=='D']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='black',label='COMPANY D')
    plt.legend(loc='best')
    
    fig1=plt.gcf()
    plotly_fig1 = tls.mpl_to_plotly(fig1)
    plotly_fig1['layout']['width'] = 870
    plot_div1 = plot(plotly_fig1, output_type='div', include_plotlyjs=False)

    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[(data['Destination']=='GUJRAT')]
    demA=x1.groupby('Month').mean()
    
    plt.figure()
    
    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='red',label='GUJRAT')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Destination']=='DELHI']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='blue',label='DELHI')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Destination']=='TAMIL NADU']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='green',label='TAMIL NADU')
    y=['Profit']
    datay=data[y]

    #prediction of Quantity_Demanded mean monthly of A
    x1=data.loc[data['Destination']=='ASSAM']
    demA=x1.groupby('Month').mean()

    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='black',label='ASSAM')
    plt.title('Place-wise Quantity Demand Analysis')
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Quantity Demanded")
    fig2=plt.gcf()
    plotly_fig2 = tls.mpl_to_plotly(fig2)
    plotly_fig2['layout']['width'] = 650
    plot_div2 = plot(plotly_fig2, output_type='div', include_plotlyjs=False)

    x1=data.loc[data['Population']>=400]
    demA=x1.groupby('Month').mean()
    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='red',label='Population more than 4Cr.')
    x1=data.loc[data['Population']<200]
    demA=x1.groupby('Month').mean()
    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='blue',label='Population less than 2Cr.')
    x1=data.loc[(data['Population']>=200) & (data['Population']<400)]
    demA=x1.groupby('Month').mean()
    plt.plot(data['Month'].unique(),demA['Quantity_Demanded'],color='black',label='Population between 2Cr. and 4 Cr.')
    plt.title('Population-wise Quantity Demand Analysis')
    plt.legend(loc='best')
    plt.xlabel("Month")
    plt.ylabel("Quantity Demanded")
    fig3=plt.gcf()
    plotly_fig3 = tls.mpl_to_plotly(fig3)
    plotly_fig3['layout']['width'] = 650
    plot_div3 = plot(plotly_fig3, output_type='div', include_plotlyjs=False)
    
    x1=data.loc[data['Ratings']==5]
    x2=data.loc[data['Ratings']==4]
    x3=data.loc[data['Ratings']==3]
    x4=data.loc[data['Ratings']==2]
    x5=data.loc[data['Ratings']==1]
    b=data['Ratings'].unique()


    l=[len(x1),len(x2),len(x3),len(x4),len(x5)]
    
    plt.figure()
    
    
    plt.bar(b,l)
    plt.xticks(list(range(1,6)),['5star','4 star','3 star','2 star','1 star'])
    
    plt.ylabel('Frequency')
    plt.xlabel('Rating')
    
    fig4=plt.gcf()
    plotly_fig4 = tls.mpl_to_plotly(fig4)
    plotly_fig4['layout']['width'] = 1000

    plot_div4 = plot(plotly_fig4, output_type='div', include_plotlyjs=False)
    
    return plot_div1, plot_div2, plot_div3, plot_div4