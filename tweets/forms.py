from django import forms

class TweetForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'class':'form-control'}),max_length=160)
	country = forms.CharField(widget=forms.HiddenInput())

class SearchForm(forms.Form):
	query = forms.CharField(label="Enter a keyword to search for", widget=forms.TextInput(attrs={'size':32,'class':'form-control mb-2 mr-sm-2', 'id':'search-query', 'placeholder':'search tweets...'}))