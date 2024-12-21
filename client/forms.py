from django import forms
from . import models


class servicerequest(forms.ModelForm):
    class Meta:
        model = models.servicerequest
        fields = "__all__"
        exclude = ('service','user','status')

class confirmorder(forms.ModelForm):
    class Meta:
        model = models.confirmorder
        fields = "__all__"
        exclude = ('product','user',)