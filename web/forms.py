from django import forms

BUSTYPE = (
    ('Volvo', 'Volvo'),
    ('Ordinary', 'Ordinary'),
)

BUSTO = (
    ('Ajmer', 'Ajmer'),
    ('Chandigarh', 'Chandigarh'),
    ('Delhi', 'Delhi'),
)

BUSFROM = (
    ('Delhi', 'Delhi'),
    ('Jaipur', 'Jaipur'),
    ('Ajmer', 'Ajmer'),
)


class FormFindBus(forms.Form):
    bus_type = forms.CharField(widget=forms.Select(choices=BUSTYPE), required=True,)
    bus_from = forms.CharField(widget=forms.Select(choices=BUSFROM), required=True,)
    bus_to = forms.CharField(widget=forms.Select(choices=BUSTO), required=True)
    date = forms.DateField(required=True) 
    
    def clean(self):
        if 'bus_from' in self.cleaned_data and 'bus_to' in self.cleaned_data and self.cleaned_data['bus_from'] == self.cleaned_data['bus_to']:
            raise forms.ValidationError("From and To are same")
        return self.cleaned_data
    
