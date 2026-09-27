from django import forms
from . models import Todo

class TodoForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField()



class updateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title' , 'content')