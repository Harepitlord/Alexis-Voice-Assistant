from django.contrib.auth import get_user_model

class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):

        User = get_user_model()
        try:
            print(User.objects.get(email=username))
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.is_active and user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
