from django import forms
from django.forms import ModelForm, widgets
from blog.models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=['title','description','content']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','id':'mytextarea'})
        }
        

        

 
        
         