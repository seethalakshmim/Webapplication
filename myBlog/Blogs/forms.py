from .models import comment_post
from django import forms

#Class to accept visitor comments
class commentform(forms.ModelForm):
    class Meta:
        model=comment_post                                  #Form class from a Django model
        fields=('name','email','comments')
