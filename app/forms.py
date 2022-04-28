"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class PoolForm(forms.Form):
    #name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    name = forms.CharField(label='', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class':'text_form',}))
    product = forms.ChoiceField(label='Вам понравилась наша продукция', choices=[('1','Да'),('2','Нет')], widget = forms.RadioSelect, initial=1)
    score = forms.ChoiceField(label='Как вы оцените наше обслуживание', choices=(('1','Отлично'),('2','Что-то среднее'),('3','Плохо')), initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        tabels = {'text': "Комментарий"}

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}