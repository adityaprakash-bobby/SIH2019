from django import forms
from .models import War, Uploaddata
from django.contrib.auth.models import User


class TableUpdateForm(forms.ModelForm):
    class Meta:
        model = War
        fields = ['war_id','war_name','war_type','side1_code','side1_name','side2_code','side2_name','start_year1','start_month1','start_day1','end_year1','end_month1','end_day1','start_year2','start_month2','start_day2','end_year2','end_month2','end_day2','previous_war','initiation','intervention','combat_location','state_fatalities','nonstate_fatalities','outcome','next_war']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UploadCSV(forms.ModelForm):
	class Meta:
		model = Uploaddata
		fields = ['upload']

class PredictionForm(forms.Form):

	product = forms.ChoiceField(label='Product', choices=[('A','A'),
                                                          ('B','B')])
	date_predict = forms.IntegerField(label='Number of days to predict')
	month = forms.ChoiceField(label='Month', choices=[(1, 'January'),
													  (2, 'February'),
													  (3, 'March'),
													  (4, 'April'),
													  (5, 'May'),
													  (6, 'June'),
													  (7, 'July'),
													  (8, 'August'),
													  (9, 'September'),
													  (10, 'October'),
													  (11, 'November'),
													  (12, 'December')])

    # def __init__(self, prod_choices, *args, **kwargs):
    #     super(PredictionForm, self).__init__(*args, **kwargs)

    #     self.fields['product'].choices = prod_choices

class AnalysisForm(forms.Form):
	type_analysis = forms.ChoiceField(label='Analysis', choices=[('R and D', 'R and D'),
																 ('Quantity Demanded', 'Quantity Demanded'),
																 ('Labour Wages', 'Labour Wages'),
																 ('Energy', 'Energy'),
																 ('Taxes', 'Taxes'),
																 ('Transport', 'Transport'),
																 ('Production', 'Production')])
	product = forms.ChoiceField(label='Product', choices=[('A','A'),
                                                          ('B','B'),
														  ('C','C'),
														  ('D','D')])

class AnalysisSeasonalForm(forms.Form):
    product = forms.ChoiceField(label='Product', choices=[('A','A'),
                                                           ('B','B')])

class AnalysisPlaceForm(forms.Form):
    product = forms.ChoiceField(label='Product', choices=[('A','A'),
                                                          ('B','B')])
    month = forms.ChoiceField(label='Month', choices=[(1, 'January'),
													  (2, 'February'),
													  (3, 'March'),
													  (4, 'April'),
													  (5, 'May'),
													  (6, 'June'),
													  (7, 'July'),
													  (8, 'August'),
													  (9, 'September'),
													  (10, 'October'),
													  (11, 'November'),
													  (12, 'December')])
    destination = forms.ChoiceField(label="Location", choices=[('SURAT', 'SURAT'),
                                                               ('AHMEDABAD', 'AHMEDABAD'),
                                                               ('VADODARA', 'VADODARA'),
                                                               ('GANDHINAGAR', 'GANDHINAGAR')])

class AnalysisPLForm(forms.Form):
	product = forms.ChoiceField(label='Product', choices=[('A','A'),
                                                          ('B','B'),
														  ('C','C'),
														  ('D','D')])