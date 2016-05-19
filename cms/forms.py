from django.forms import ModelForm
from django import forms
from cms.models import Book,Impression

class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('func_name', 'program_name', 'tag','author','Github',)

class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )





