from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreerUser(UserCreationForm):
    class Meta:
        model= Userfields=['username','email','password1']