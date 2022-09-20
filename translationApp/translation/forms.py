from django import forms

class TranslationForm(forms.Form):
# 英語→日本語のバージョンも作る
    sentence = forms.CharField(label='翻訳(日本語→英語)', widget=forms.Textarea(), required=True)