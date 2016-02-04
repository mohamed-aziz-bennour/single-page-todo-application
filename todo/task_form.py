from django import forms
from todo.models import Todo


class PostForm(forms.ModelForm):
    class Meta:
        model = Todo 
        fields = ['task'] 