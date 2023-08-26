from django import forms

# creating a form
class QuestionForm(forms.Form):
	question = forms.CharField(max_length = 300)
	option1 = forms.CharField(max_length = 200)
	option2 = forms.CharField(max_length = 200)
	option3 = forms.CharField(max_length = 200)
	option4 = forms.CharField(max_length = 200)
	correct_option = forms.CharField(max_length = 200)

class MyForm(forms.Form):
    my_radio = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')], widget=forms.RadioSelect)
	
