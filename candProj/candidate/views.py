from django.core.mail import send_mail
from rest_framework import viewsets
from validate_email import validate_email
from .models import Candidat
from .serializers import CadidatAppSerializer


class CandidatViewSet(viewsets.ModelViewSet):

    queryset = Candidat.objects.all()
    serializer_class = CadidatAppSerializer

    def perform_create(self, serializer):
        recipient = serializer.validated_data.get('email')

        is_valid = validate_email(email_address=recipient, check_regex=True, check_mx=True,
                                  from_address='tech.test162@gmail.com', helo_host='smtp.gmail.com', smtp_timeout=10,
                                  dns_timeout=10, debug=False)

        if is_valid:
            email_cand(recipient)
            serializer.save(email_status=Candidat.YES)

        else:
            serializer.save(email_status=Candidat.NO)


def email_cand(recipient):

    return send_mail(
        'Validation',
        'Merci pour la validation de Votre candidature',
        'tech.test162@gmail.com',
        [recipient],
        fail_silently=False,
    )


