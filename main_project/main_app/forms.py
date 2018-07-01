from django import forms
from django.core import validators
    
# Form fields
class Text_input(forms.Form):
    text_input = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter text here...',
            'rows' : '3',
        }),
    )
    
class Choice_input(forms.Form):
    choice_input = forms.ChoiceField(
        label = '',
        choices=(
            ('0', 'Select options'), 
            ('1', 'Option 1'),
            ('2', 'Option 2'), 
            ('3', 'Option 3')
        ),
        widget=forms.Select(attrs={
            'class' : 'custom-select mb-2 mr-sm-2 mb-sm-0',
            'id' : 'inlineFormCustomSelectPref',
        }),
    )