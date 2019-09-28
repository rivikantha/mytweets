from django import forms

class TweetForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'class':'form-control'}),max_length=160)
	country = forms.CharField(widget=forms.HiddenInput())