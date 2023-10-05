from django import forms
from . import models



class WatchShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = '__all__'