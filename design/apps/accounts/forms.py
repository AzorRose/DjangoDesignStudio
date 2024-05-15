from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

class SignUpForm(UserCreationForm):
   
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = None
        self.fields['last_name'].initial = None
        self.fields['patronymic'].initial = None
   
    
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', \
            'patronymic', 'phone_number', 'email')

class SignInForm(AuthenticationForm):
    pass