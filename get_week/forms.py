from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class DateForm(forms.Form):
    date = forms.DateField(
        widget=AdminDateWidget(
            attrs={'placeholder': '2020-12-12'}
        )
    )
