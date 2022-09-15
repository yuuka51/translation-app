from django import forms

class TranslationForm(forms.Form):

    sentence = forms.CharField(label='翻訳(日本語→英語)', widget=forms.Textarea(), required=True)