from django import forms
from django.core import validators
from LoanApp.models import UserDetails,UserLoan
from datetime import date

class UserDetailsForm(forms.ModelForm):
    class Meta():
        model=UserDetails
        fields="__all__"
    Allot=forms.IntegerField(initial=100000,widget=forms.HiddenInput())
    def clean(self):
        all_cleaned_data=super().clean()
        DOB=all_cleaned_data['DOB']
        
        today=date.today()
        age=today-DOB

        if((age.days/365.25)<18):
            raise forms.ValidationError("invalid Age")
class UserLoanForm(forms.ModelForm):
    class Meta():
        model=UserLoan
        fields="__all__"    
    rate=forms.ChoiceField(choices=[(x, x) for x in range(1, 15)]) 

