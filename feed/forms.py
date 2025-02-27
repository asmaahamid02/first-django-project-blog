from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(min_length=100, widget=forms.Textarea(attrs={"rows": "5"}))
    image = forms.FileField()
