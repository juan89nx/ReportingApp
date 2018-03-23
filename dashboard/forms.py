from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

class GetReportingForm(forms.Form):
    #cada atributo corresponde con el atributo name en el html
    observaciones = forms.CharField(label='ovserbaciones', max_length=250)