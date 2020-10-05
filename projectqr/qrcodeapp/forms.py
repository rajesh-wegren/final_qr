from django import forms
from qrcodeapp.models import Qrcode

# class QrForm(forms.Form):
#     # TODO: Define form fields here
#     url = forms.CharField()
class QrForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields =['user_url']
