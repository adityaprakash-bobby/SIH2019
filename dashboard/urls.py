from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_all, name='dash-all'),
    path('dashforms/', views.dash_home, name='dash-home'),
    path('analyse/', views.data_analysis, name='dash-analyse'),
    path('analysePL/', views.analysis_profitloss, name='dash-analyse-PL'),
    path('analyseseasonal/', views.dash_analysis_season, name='dash-analyse-seasonal'),
    path('analyseplacewise/', views.dash_analysis_place, name='dash-analyse-place'),
    path('predict/', views.dash_predict, name='dash-predict'),
    path('update/', views.update_table, name='update-table')
]
