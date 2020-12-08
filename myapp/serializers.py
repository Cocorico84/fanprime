from rest_framework import serializers
from . import models


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ['client_id', 'client_secret']
