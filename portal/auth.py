from .models import User

class PasswordBasedBackend(object):
    def authenticate(self, request, username=None, password=None):
        if (username is None) or (password is None):
            return None
        try:
            user = User.objects.get(roll_no=username)
        except User.DoesNotExist:
            # create a new user
            return None
        # assume that the password is right
        return user

    def get_user(self, roll_no):
        try:
            return User.objects.get(roll_no=roll_no)
        except User.DoesNotExist:
            return None


from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import UserSession


def user_logged_in_handler(sender, request, user, **kwargs):
    UserSession.objects.get_or_create(
        user = user,
        session_id = request.session.session_key
    )

def user_logged_out_handler(sender, request, user, **kwargs):
    sessions = UserSession.objects.filter(user=user)
    for sess in sessions:
        sess.session.delete()

# user_logged_in.connect(user_logged_in_handler)
# user_logged_out.connect(user_logged_out_handler)
