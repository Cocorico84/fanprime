from django import forms
from main import get_user, get_token


class SearchForm(forms.Form):
    client_id = forms.CharField()
    client_secret = forms.CharField()
    user = forms.CharField()

    def search(self):
        user = self.cleaned_data['user']
        client_id = self.cleaned_data['client_id']
        client_secret = self.cleaned_data['client_secret']
        token = get_token(client_id=client_id, client_secret=client_secret)
        url = get_user(token, client_id, user)
        return url

