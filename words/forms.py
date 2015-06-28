# this file handles form input in Python

from django import forms

class MessageForm(forms.Form):
	content = forms.CharField(label='content', max_length=500)
