from django import forms
from . import models




class productform(forms.ModelForm):
    class Meta:
        model = models.productmodel
        fields = "__all__"

class categoryform(forms.ModelForm):
    class Meta:
        model = models.categorymodel
        fields = "__all__"


class usecategoryform(forms.ModelForm):
    class Meta:
        model = models.usecategorymodel
        fields = "__all__"



# --------------For Services-----------------
class storeform(forms.ModelForm):
    class Meta:
        model = models.storemodel
        fields = "__all__"
