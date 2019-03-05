import django.forms as forms


class AddJobForm(forms.Form):
    title = forms.CharField(max_length=50)
    minsal = forms.IntegerField(min_value=5000, max_value=1000000)
