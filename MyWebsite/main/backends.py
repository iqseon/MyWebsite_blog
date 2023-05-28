from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.models import User
from django.db.models import Q


class EmailBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargas):
        try:
            user = User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            pass

        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by(id).first()

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user