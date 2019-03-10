from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required, permission_required
from django.http import HttpResponse
from .forms import TableUpdateForm, PredictionForm, AnalysisSeasonalForm, AnalysisPlaceForm, UploadCSV, UserUpdateForm, AnalysisForm, AnalysisPLForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File

# for analysis
from .prediction import *
from .analysis import *
from .map import *

@login_required
def dash_all(request):
    plotmap = printmap()
    plot_div1, plot_div2, plot_div3, plot_div4 = graphs1(file="SIH2_1.csv")

    ctx = {
        'mapdata': plotmap,
        'plot_div1' : plot_div1,
        'plot_div2' : plot_div2,
        'plot_div3' : plot_div3,
        'plot_div4' : plot_div4
    }

    return render(request, 'dashboard/dashboard_all.html', ctx)

@login_required
def dash_analysis_season(request):
    if request.method == 'POST':
        form = AnalysisSeasonalForm(request.POST)
        if form.is_valid():
            f = open(settings.MEDIA_ROOT + '/' + request.user.uploaddata.upload.name, 'rb')
            plot_div = analysis_seasonal(form.cleaned_data['product'], data=f)
    # plot_div_AR = returnAR('A', 8, 10)

    ctx = {
        'title' : 'Dashboard - Analysis',
        'plot':plot_div,
        'head':'Seasonal Analysis',
        'product':form.cleaned_data['product']
    }
    return render(request, 'dashboard/dash_analyse.html', ctx)

@login_required
def dash_analysis_place(request):
    if request.method == 'POST':
        form = AnalysisPlaceForm(request.POST)
        if form.is_valid():
            f = open(settings.MEDIA_ROOT + '/' + request.user.uploaddata.upload.name, 'rb')
            plot_div = analysis_destination(form.cleaned_data['product'], int(form.cleaned_data['month']), form.cleaned_data['destination'],data=f)

    ctx = {
        'title' : 'Dashboard - Analysis',
        'plot':plot_div,
        'head': 'Supply demand analysis',
        'product':form.cleaned_data['product'],
        'location': ' at location ' + form.cleaned_data['destination']
    }
    return render(request, 'dashboard/dash_analyse.html', ctx)

@login_required
def data_analysis(request):
    if request.method == 'POST':
        form = AnalysisForm(request.POST)
        if form.is_valid():
            # f = open(settings.MEDIA_ROOT + '/' + request.user.uploaddata.upload.name, 'rb')
            plot_div, head = creategraph(form.cleaned_data['product'], form.cleaned_data['type_analysis'], filename='SIH2.csv')
    ctx = {
        'title' : 'Dashboard - Analysis',
        'plot':plot_div,
        'head':head,
        'product':form.cleaned_data['product']
    }
    return render(request, 'dashboard/dash_analyse.html', ctx)

@login_required
def analysis_profitloss(request):
    if request.method == 'POST':
        form = AnalysisPLForm(request.POST)
        if form.is_valid():
            plot_div = profitloss(form.cleaned_data['product'], filename='SIH2.csv')
    
    ctx = {
        'title' : 'Dashboard - Analysis',
        'plot':plot_div,
        'head': 'Profit/Loss',
        'product':form.cleaned_data['product']
    }

    return render(request, 'dashboard/dash_analyse.html', ctx)

@login_required
def dash_predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            f = open(settings.MEDIA_ROOT + '/' + request.user.uploaddata.upload.name, 'rb')
            print(type(form.cleaned_data['product']))
            print(type(form.cleaned_data['month']))
            print(form.cleaned_data['date_predict'])
            # df = pd.read_csv(f)
            # x1 = df['Product_Name'].unique()
            # prod_choices = []
            # for x in x1:
            #     prod_choices.append((x, x))
            # form1 = PredictionForm(prod_choices)
            plot_div_AR = returnAR(form.cleaned_data['product'], int(form.cleaned_data['month']), int(form.cleaned_data['date_predict']), dataset=f)
        ctx = {
            'title' : 'Dashboard - Prediction',
            'plot_div_AR':plot_div_AR,
            'head': 'Prediction of Sales',
            'product': form.cleaned_data['product'],
            'days': str(form.cleaned_data['date_predict'])
        }
        return render(request, 'dashboard/dash_predict.html', ctx)


@login_required
def dash_home(request):
    # f = open(settings.MEDIA_ROOT + '/' + request.user.uploaddata.upload.name, 'rb')
    # df = pd.read_csv(f)
    # x1 = df['Product_Name'].unique()
    # prod_choices = []
    # for x in x1:
    #     prod_choices.append((x, x))
    #     form = PredictionForm(prod_choices)
    form_1 = PredictionForm() 
    form_2 = AnalysisSeasonalForm()
    form_3 = AnalysisPlaceForm()
    form_4 = AnalysisForm()
    form_5 = AnalysisPLForm()

    ctx = {
        'form_1' : form_1,
        'form_2' : form_2,
        'form_3' : form_3,
        'form_4' : form_4,
        'form_5' : form_5
    }

    return render(request, 'dashboard/dash_home.html', ctx)

# @permission_required('admin.can_add_log_entry')
@login_required
def update_table(request):

    if request.method == 'POST':
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = UploadCSV(request.POST, request.FILES, instance=request.user.uploaddata)
        if form1.is_valid() and form2.is_valid():

            form1.save()
            form2.save()

        return redirect('dash-home')
    else:
        form1 = UserUpdateForm(instance=request.user)
        form2 = UploadCSV(instance=request.user.uploaddata)
        form3 = TableUpdateForm()
    ctx = {
        'form1':form1,
        'form2':form2,
        'form3':form3
    }
    return render(request, 'dashboard/update_table.html', ctx)

