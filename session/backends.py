from django.contrib.auth import get_user_model

from django.contrib.auth.backends import ModelBackend

from django.db.models import Q

User = get_user_model()


class CustomBackend(ModelBackend):

    def authenticate(self, request, username, password, **kwargs):

        if not username or not password:

            return None

        try:
            
            user = User.objects.get(Q(username = username) | Q(email = username))

        except User.DoesNotExists:

            return None

        if user.check_password(password):

            return user

        return None

    def get_user(self, id):
        try:

            return User.objects.get(id = id)

        except User.DoesNotExists:

            return None