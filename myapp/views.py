from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Credential
from .serializers import CredentialSerializer
from .forms import SearchForm


class CredentialViewSet(viewsets.ModelViewSet):
    '''
    Allow to store all of client id and client secret of the differents apps
    '''
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [permissions.IsAuthenticated]


def search(request):
    result = {}
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            result = form.search()
    else:
        form = SearchForm()

    return render(request, "templates/search.html", {'form': form, 'search': result})
