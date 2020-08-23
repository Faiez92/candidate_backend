from rest_framework import serializers
from .models import Candidat
from validate_email import validate_email


class CadidatAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ('id',
                  'nom',
                  'prenom',
                  'email',
                  'date_naiss',
                  'tel',
                  'disp',
                  'exp',
                  'msg',
                  'cv',
                  'cand_status',
                  'email_status',
                  )

