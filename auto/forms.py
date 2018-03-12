#-*- coding: utf-8 -*-


from django import forms
from .models import *

class CommentsForm(forms.ModelForm):

    author = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Имя...'}), required=True)
    text = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                          'placeholder': 'Ваш отзыв о работе...'}),
                             required=True)
    honey = forms.CharField(widget=forms.HiddenInput(attrs={'value': ''}), required=False)

    class Meta:
        model = Comments
        fields = ('author',  'text',)
